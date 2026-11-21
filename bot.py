bot.py

import os
import telebot
from telebot import types

TOKEN = os.environ.get("8890663489:AAGT4d3qPpl46GSUiK4pLJRmB-8SYp1pFgs")

if not TOKEN:
    raise ValueError("Не задан BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.row("🎬 Каталог", "🔎 Поиск")
    keyboard.row("❤️ Избранное", "✨ Рекомендации")
    keyboard.row("ℹ️ О боте")

    bot.send_message(
        message.chat.id,
        "🍿 ANIME CINEMA\n\n"
        "Добро пожаловать в твой аниме-кинотеатр!\n\n"
        "Выбери раздел ниже 👇",
        reply_markup=keyboard
    )

@bot.message_handler(func=lambda m: True)
def menu(message):
    text = message.text

    if text == "🎬 Каталог":
        bot.send_message(
            message.chat.id,
            "🎬 Каталог аниме скоро откроется!"
        )

    elif text == "🔎 Поиск":
        bot.send_message(
            message.chat.id,
            "🔎 Напиши название аниме."
        )

    elif text == "❤️ Избранное":
        bot.send_message(
            message.chat.id,
            "❤️ Здесь будут твои любимые аниме."
        )

    elif text == "✨ Рекомендации":
        bot.send_message(
            message.chat.id,
            "✨ Скоро здесь появятся рекомендации!"
        )

    elif text == "ℹ️ О боте":
        bot.send_message(
            message.chat.id,
            "🌸 ANIME CINEMA\nТвой мир аниме!"
        )

    else:
        bot.send_message(
            message.chat.id,
            "Выбери раздел в меню 👇"
        )

print("ANIME CINEMA запущен!")
bot.infinity_polling()
