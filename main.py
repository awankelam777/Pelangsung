
import telebot

BOT_TOKEN = "7851637498:AAEcswBnyx55_rRM2YeKqZBhL7RhWvs7oTg"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Halo! Bot Telegram kamu sudah aktif.")

bot.polling()
