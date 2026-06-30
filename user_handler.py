
async def service_select(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    context.user_data['service_type'] = query.data
    await query.edit_message_text(f"আপনি {query.data.upper()} বেছে নিয়েছেন। এখন আপনার নম্বর বা ফাইলটি পাঠান।")

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
    await update.message.reply_text(f"✅ আপনার {service.upper()} নম্বরটি সেভ হয়েছে!")
