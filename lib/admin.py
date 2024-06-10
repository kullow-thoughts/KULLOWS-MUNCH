import sqlite3

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add Menu Item")
        print("2. Update Menu Item")
        print("3. Remove Menu Item")
        print("4. View Menu")
        print("5. Exit Admin Menu")

        choice = input("Choose an option: ")
        if choice == '1':
            add_menu_item()
        elif choice == '2':
            update_menu_item()
        elif choice == '3':
            remove_menu_item()
        elif choice == '4':
            view_menu()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def add_menu_item():
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    name = input("Enter the name of the new item: ")
    price = float(input("Enter the price of the new item: "))

    try:
        cursor.execute("INSERT INTO menu_items (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        print("Menu item added successfully!")
    except sqlite3.IntegrityError:
        print("Menu item already exists.")
    
    conn.close()

def update_menu_item():
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    item_id = input("Enter the ID of the item to update: ")
    new_name = input("Enter the new name: ")
    new_price = float(input("Enter the new price: "))

    cursor.execute("UPDATE menu_items SET name=?, price=? WHERE id=?", (new_name, new_price, item_id))
    conn.commit()
    print("Menu item updated successfully!")
    conn.close()

def remove_menu_item():
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    item_id = input("Enter the ID of the item to remove: ")

    cursor.execute("DELETE FROM menu_items WHERE id=?", (item_id,))
    conn.commit()
    print("Menu item removed successfully!")
    conn.close()

def view_menu():
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu_items")
    items = cursor.fetchall()
    print("Menu:")
    for item in items:
        print(f"{item[0]}. {item[1]} - ${item[2]}")
    conn.close()
