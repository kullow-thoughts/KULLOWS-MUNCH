import sqlite3

def init_db():
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS menu_items (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE,
        price REAL NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        items TEXT NOT NULL,
        total_price REAL NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    menu_items = [
        ('Pizza', 8.99),
        ('Burger', 5.99),
        ('Salad', 4.99),
        ('Pasta', 7.99),
        ('Sushi', 12.99),
        ('Steak', 15.99),
        ('Tacos', 3.99),
        ('Sandwich', 4.49),
        ('Ice Cream', 2.99),
        ('Coffee', 1.99),
        ('Tea', 1.49),
        ('Soda', 1.99)
    ]

    for item in menu_items:
        try:
            cursor.execute("INSERT INTO menu_items (name, price) VALUES (?, ?)", item)
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
