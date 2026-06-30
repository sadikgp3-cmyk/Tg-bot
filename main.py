import logging
from telegram.ext import ApplicationBuilder
from config import TOKEN
from handlers.user_handler import user_router
from handlers.admin_handler import admin_router

logging.basicConfig(level=logging.INFO)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(user_router)
    app.add_handler(admin_router)
    
    print("🚀 বট চালু হয়েছে...")
    app.run_polling()

if __name__ == '__main__':
    main()
from handlers.user_handler import service_select, receive_number
from telegram.ext import CallbackQueryHandler, MessageHandler, filters

# হ্যান্ডলার যোগ করার জায়গায় এগুলো লিখুন
app.add_handler(CallbackQueryHandler(service_select, pattern='^(wa|tg|ig|fb)$'))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_number))
