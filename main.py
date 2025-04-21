import telebot
from flask import Flask
from threading import Thread

# Ganti ini dengan token bot kamu
API_TOKEN = 'PASTE_TOKEN_KAMU_DI_SINI'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hai! Aku hidup di Glitch sekarang.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=3000)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()
bot.infinity_polling()