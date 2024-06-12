import sqlite3

def create_tables():
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seasonal_flavors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ingredients TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer_suggestions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor TEXT NOT NULL,
            suggestion TEXT,
            allergens TEXT
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS allergens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flavor_id INTEGER,
            quantity INTEGER,
            FOREIGN KEY(flavor_id) REFERENCES seasonal_flavors(id)
        )
    ''')
    
    conn.commit()
    conn.close()

create_tables()
