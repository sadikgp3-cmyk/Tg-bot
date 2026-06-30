from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # শুধু বাটনগুলো থাকবে, এখানে অন্য কোনো ফাংশন কল করবেন না
    keyboard = [
        [InlineKeyboardButton("📱 WhatsApp", callback_data='wa'), InlineKeyboardButton("✈️ Telegram", callback_data='tg')],
        [InlineKeyboardButton("📸 Instagram", callback_data='ig'), InlineKeyboardButton("📘 Facebook", callback_data='fb')],
        [InlineKeyboardButton("⚙️ Admin Panel", callback_data='admin')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # ইউজারকে শুধু মেনু দেখানো হবে
    await update.message.reply_text(
        "✨ স্বাগতম! আপনার সার্ভিসটি বেছে নিন:", 
        reply_markup=reply_markup
    )

# সার্ভিস সিলেক্ট করার ফাংশন
async def service_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data['service_type'] = query.data
    await query.answer()
    await query.edit_message_text(f"আপনি {query.data.upper()} বেছে নিয়েছেন। এখন আপনার নম্বর বা ফাইলটি পাঠান।")

# নম্বর রিসিভ করার ফাংশন
import sqlite3
async def receive_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    service = context.user_data.get('service_type', 'none')
    if service == 'none':
        await update.message.reply_text("প্রথমে মেনু থেকে একটি সার্ভিস সিলেক্ট করুন।")
        return
    
    data = update.message.text
    conn = sqlite3.connect('numbers.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO user_numbers (user_id, service, data) VALUES (?, ?, ?)', 
                   (update.effective_user.id, service, data))
    conn.commit()
    conn.close()
    await update.message.reply_text(f"✅ আপনার {service.upper()} নম্বরটি সফলভাবে সেভ হয়েছে!")
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from handlers.user_handler import start, service_select, receive_number
from handlers.admin_handler import admin_menu, admin_stats, admin_broadcast

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    TOKEN = "আপনার_বট_টোকেন_এখানে_দিন"
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(admin_menu, pattern='admin'))
    app.add_handler(CallbackQueryHandler(admin_stats, pattern='admin_stats'))
    app.add_handler(CallbackQueryHandler(service_select, pattern='^(wa|tg|ig|fb)$'))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_number))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
