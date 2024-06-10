import sqlite3

def place_order(user):
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    order_items = []
    total_price = 0.0

    while True:
        item_id = input("Enter the item number to order (or 'q' to finish): ")
        if item_id.lower() == 'q':
            break

        cursor.execute("SELECT * FROM menu_items WHERE id=?", (item_id,))
        item = cursor.fetchone()
        if item:
            order_items.append(item[1])
            total_price += item[2]
        else:
            print("Invalid item number, please try again.")

    if order_items:
        cursor.execute("INSERT INTO orders (user_id, items, total_price) VALUES (?, ?, ?)", (user[0], ", ".join(order_items), total_price))
        conn.commit()
        print(f"Order placed! Total price: ${total_price}")
    else:
        print("No items ordered.")

    conn.close()

def view_order_summary(user):
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders WHERE user_id=?", (user[0],))
    orders = cursor.fetchall()
    for order in orders:
        print(f"Order #{order[0]}: {order[2]} - Total: ${order[3]}")
    conn.close()
