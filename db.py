
import sqlite3

def create_tables():
    conn = sqlite3.connect('happy_burguer.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS clients (
        clave TEXT PRIMARY KEY,
        name TEXT,
        address TEXT,
        email TEXT,
        tel TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS menu (
        clave TEXT PRIMARY KEY,
        name TEXT,
        price REAL
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        client TEXT,
        product TEXT,
        price real
    )''')
    
    conn.commit()
    conn.close()