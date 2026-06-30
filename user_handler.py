from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("📱 WhatsApp", callback_data='wa'), InlineKeyboardButton("✈️ Telegram", callback_data='tg')],
        [InlineKeyboardButton("⚙️ Admin Panel", callback_data='admin')]
    ]
    await update.message.reply_text("✨ স্বাগতম! সার্ভিস বেছে নিন:", reply_markup=InlineKeyboardMarkup(keyboard))

async def service_select(update, context):
    query = update.callback_query
    context.user_data['service_type'] = query.data
    await query.edit_message_text(f"আপনি {query.data.upper()} বেছে নিয়েছেন। এখন নম্বর পাঠান।")

async def receive_number(update, context):
    # ডাটাবেসে সেভ করার কোড এখানে থাকবে
    await update.message.reply_text("✅ সেভ হয়েছে!")
