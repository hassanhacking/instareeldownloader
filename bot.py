import telebot
import yt_dlp
import os


BOT_TOKEN = "8109058591:AAHDIQJg7SFC-tQ3vHApvtS-NzPBdPi86k8"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "give me your url")

@bot.message_handler(func=lambda msg: "instagram.com/reel/" in msg.text)
def download_reel(message):
    url = message.text.strip()
    chat_id = message.chat.id

    bot.send_message(chat_id, "loding .....")

    ydl_opts = {
        'outtmpl': 'reel.%(ext)s',
        'format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        with open(filename, 'rb') as video:
            bot.send_video(chat_id, video)

        os.remove(filename)

    except Exception as e:
        bot.send_message(chat_id, f"error\n{str(e)}")

@bot.message_handler(func=lambda msg: True)
def fallback(message):
    bot.reply_to(message, "just give me the reel url📎")

bot.polling()
