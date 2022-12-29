import telebot
import time
import os


TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(m, res=False):
        bot.send_message(m.chat.id, 'Йоу, я на связи')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    for i in range (1, 365):
    # Отправка ответа
        bot.send_message(message.chat.id, '/pidor')
        time.sleep(86400)
# Запускаем бота
bot.polling(none_stop=True, interval=0)