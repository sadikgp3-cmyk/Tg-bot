
import logging
from telegram.ext import ApplicationBuilder
from config import TOKEN
from handlers.user_handler import user_router
from handlers.admin_handler import admin_router

# Logging setup for clean debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    print("🚀 বটের ইঞ্জিন স্টার্ট হচ্ছে...")
    app = ApplicationBuilder().token(TOKEN).build()

    # হ্যান্ডলার রেজিস্টার করা
    app.add_handler(user_router)
    app.add_handler(admin_router)

    print("✅ বট এখন লাইভ! (আপনার আইডি: 8514892358)")
    app.run_polling()

if __name__ == '__main__':
    main()
