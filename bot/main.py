import telebot
import time
import os


TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
        bot.send_message(message.chat.id, '')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    for i in range (1, 365):
        bot.send_message(message.chat.id, '')
        time.sleep(86400)

bot.polling(none_stop=True, interval=0)