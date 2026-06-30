from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from config import ADMIN_IDS

async def admin_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    
    # সিকিউরিটি চেক
    if query.from_user.id not in ADMIN_IDS:
        await query.answer("❌ আপনি অ্যাডমিন নন!", show_alert=True)
        return

    # বাটন ডিজাইন
    keyboard = [
        [InlineKeyboardButton("📢 Broadcast", callback_data='admin_broadcast')],
        [InlineKeyboardButton("📊 User Stats", callback_data='admin_stats')],
        [InlineKeyboardButton("🔙 Back", callback_data='start')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        "👑 **ADMIN CONTROL PANEL**\n\nনিচের অপশনগুলো থেকে বেছে নিন:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
