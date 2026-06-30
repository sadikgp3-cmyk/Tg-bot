
import sqlite3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def admin_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect('numbers.db')
    cursor = conn.cursor()
    cursor.execute("SELECT service, COUNT(*) FROM user_numbers GROUP BY service")
    stats = cursor.fetchall()
    conn.close()

    text = "📊 **সার্ভিস অনুযায়ী নম্বর লিস্ট:**\n\n"
    for service, count in stats:
        text += f"• {service.upper()}: {count} টি নম্বর\n"
    await update.callback_query.edit_message_text(text, parse_mode='Markdown')

# এটি অ্যাডমিন মেনু ফাংশনের ভেতরে বাটন হিসেবে যোগ করতে পারেন
