from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config import ADMIN_IDS
import sqlite3

async def admin_menu(update, context):
    query = update.callback_query
    if query.from_user.id not in ADMIN_IDS:
        await query.answer("আপনি অ্যাডমিন নন!")
        return
    keyboard = [
        [InlineKeyboardButton("📊 User Stats", callback_data='admin_stats')],
        [InlineKeyboardButton("📢 Broadcast", callback_data='admin_broadcast')]
    ]
    await query.edit_message_text("👑 **ADMIN CONTROL PANEL**", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def admin_stats(update, context):
    # ডাটাবেস থেকে কাউন্ট আনা
    await update.callback_query.answer("এখানে ডাটা দেখাবে")
