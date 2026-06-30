async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # শুধু মেনু বাটনগুলো থাকবে
    keyboard = [
        [InlineKeyboardButton("📱 WhatsApp", callback_data='wa'), InlineKeyboardButton("✈️ Telegram", callback_data='tg')],
        [InlineKeyboardButton("📸 Instagram", callback_data='ig'), InlineKeyboardButton("📘 Facebook", callback_data='fb')],
        [InlineKeyboardButton("⚙️ Admin Panel", callback_data='admin')]
    ]
    await update.message.reply_text(
        "✨ স্বাগতম! আপনার সার্ভিসটি বেছে নিন:", 
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
