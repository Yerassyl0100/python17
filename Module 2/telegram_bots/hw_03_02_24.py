import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    if "как тебя зовут" in message.text.lower():
        bot.reply_to(message, "Меня зовут Бот. А Вас?")
    elif "сколько тебе лет" in message.text.lower():
        bot.reply_to(message, "Я родился 02/02/2024, а Вы?")
    elif "какой твой любимый цвет" in message.text.lower():
        bot.reply_to(message, "Мой любимый цвет - синий. Как насчет вашего?")
    elif "какое твое хобби" in message.text.lower():
        bot.reply_to(message, "Мое хобби - общаться с людьми. У Вас есть хобби?")


bot.polling()
