from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("📱 WhatsApp", callback_data='wa'), InlineKeyboardButton("✈️ Telegram", callback_data='tg')],
        [InlineKeyboardButton("📸 Instagram", callback_data='ig'), InlineKeyboardButton("📘 Facebook", callback_data='fb')],
        [InlineKeyboardButton("⚙️ Admin Panel", callback_data='admin')]
    ]
    await update.message.reply_text("✨ স্বাগতম! আপনার সার্ভিসটি বেছে নিন:", reply_markup=InlineKeyboardMarkup(keyboard))

user_router = CommandHandler("start", start)
