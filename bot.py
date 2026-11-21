
import os
import telebot
from telebot import types

TOKEN = os.environ.get("8890663489:AAGT4d3qPpl46GSUiK4pLJRmB-8SYp1pFgs")

if not TOKEN:
    raise ValueError("8890663489:AAGT4d3qPpl46GSUiK4pLJRmB-8SYp1pFgs")

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
        "🍿 ДОБРО ПОЖАЛОВАТЬ В ANIME CINEMA!\n\n"
        "Твой собственный мир аниме!\n"
        "Выбери нужный раздел 👇",
        reply_markup=keyboard
    )


@bot.message_handler(func=lambda m: True)
def menu(message):
    if message.text == "🎬 Каталог":
        bot.send_message(
            message.chat.id,
            "🎬 Каталог аниме скоро появится!"
        )

    elif message.text == "🔎 Поиск":
        bot.send_message(
            message.chat.id,
            "🔎 Напиши название аниме."
        )

    elif message.text == "❤️ Избранное":
        bot.send_message(
            message.chat.id,
            "❤️ Здесь будут твои любимые аниме."
        )

    elif message.text == "✨ Рекомендации":
        bot.send_message(
            message.chat.id,
            "✨ Скоро появятся рекомендации!"
        )

    elif message.text == "ℹ️ О боте":
        bot.send_message(
            message.chat.id,
            "🌸 ANIME CINEMA\n"
            "Твой личный аниме-кинотеатр!"
        )

    else:
        bot.send_message(
            message.chat.id,
            "Выбери раздел в меню 👇"
        )


print("ANIME CINEMA запущен!")
bot.infinity_polling()
