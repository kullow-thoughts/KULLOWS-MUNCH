import sqlite3

def display_menu():
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu_items")
    items = cursor.fetchall()
    print("Menu:")
    for item in items:
        print(f"{item[0]}. {item[1]} - ${item[2]}")
    conn.close()
