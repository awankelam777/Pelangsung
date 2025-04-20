from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

BOT_TOKEN = os.getenv("7851637498:AAEcswBnyx55_rRM2YeKqZBhL7RhWvs7oTg")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hai! Kirim file ke aku, nanti aku kasih link buat kamu download langsung."
    )

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = update.message.document or update.message.photo[-1] or update.message.video or update.message.audio
    if not file:
        await update.message.reply_text("Maaf, aku nggak nemu file yang bisa diproses.")
        return

    file_info = await file.get_file()
    direct_link = f"https://api.telegram.org/file/bot{7851637498:AAEcswBnyx55_rRM2YeKqZBhL7RhWvs7oTg}/{file_info.file_path}"
    await update.message.reply_text(f"Nih link buat download langsung:\n{direct_link}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(7851637498:AAEcswBnyx55_rRM2YeKqZBhL7RhWvs7oTg).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(
        filters.Document.ALL | filters.PHOTO | filters.VIDEO | filters.AUDIO, handle_file
    ))
    print("Bot jalan di server...")
    app.run_polling()
