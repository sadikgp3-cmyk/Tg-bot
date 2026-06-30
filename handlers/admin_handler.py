from telegram import Update
from telegram.ext import CallbackQueryHandler
from config import ADMIN_IDS

async def admin_menu(update: Update, context):
    query = update.callback_query
    if query.from_user.id not in ADMIN_IDS:
        await query.answer("❌ আপনি অ্যাডমিন নন!", show_alert=True)
        return

    text = "👑 **ADMIN CONTROL PANEL**\n\n১. Broadcast\n২. User Stats\n৩. Ban User\n৪. Export Data\n৫. Welcome Msg\n৬. Maintenance\n৭. API Control\n৮. Feedback\n৯. Task Scheduler\n১০. Security"
    await query.edit_message_text(text, parse_mode='Markdown')

admin_router = CallbackQueryHandler(admin_menu, pattern='admin')
