import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)

films = [
    {"title": "Фильм 1", "url": "https://example.com/film1"},
    {"title": "Фильм 2", "url": "https://example.com/film2"},
    {"title": "Фильм 3", "url": "https://example.com/film3"}
]

def create_films_buttons():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [types.KeyboardButton(film["title"]) for film in films]
    markup.add(*buttons)
    return markup


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Выберите фильм из списка:", reply_markup=create_films_buttons())


@bot.message_handler(func=lambda message: True)
def film_search(message):
    film_title = message.text.strip()
    for film in films:
        if film["title"].lower() == film_title.lower():
            bot.send_message(message.chat.id, f"Найден фильм: {film['title']}\nСсылка: {film['url']}")
            return
    bot.send_message(message.chat.id, "Фильм не найден.")


@bot.message_handler(commands=['all_films'])
def send_all_films(message):
    films_list = "\n".join([f"{film['title']}: {film['url']}" for film in films])
    bot.send_message(message.chat.id, f"Список всех фильмов:\n{films_list}")


bot.polling()
