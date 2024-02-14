import random
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['sticker'])
def get_sticker_id(message):
    sticker_id = message.sticker.file_id
    bot.reply_to(message, f"ID стикера: {sticker_id}")


@bot.message_handler(commands=['send_me_sticker'])
def send_random_sticker(message):
    stickers = [
        'CAACAgIAAxkBAANFZcxgy5yH9DpCidcwZhnGK5juHNsAAkgAA-W5CBqPxnXZ25IcsjQE',
        'CAACAgIAAxkBAANJZcxhBZ5D4MxwXXy1NpUTiPnYgocAAp8AAw4Z7ByiAAHA8-j1N1w0BA',
        'CAACAgIAAxkBAANLZcxhMzXqmX5XnkmL9idFjgHTUJUAAuczAAL8hdBIUR9GTOirEBo0BA'
    ]

    sticker = random.choice(stickers)
    bot.send_sticker(message.chat.id, sticker)


bot.polling()