
import sqlite3

def init_db():
    conn = sqlite3.connect('numbers.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_numbers 
                      (id INTEGER PRIMARY KEY, user_id INTEGER, service TEXT, data TEXT)''')
    conn.commit()
    conn.close()
