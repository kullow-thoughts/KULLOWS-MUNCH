from database import Database

def main_menu(db):
    while True:
        print("\n--- Main Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register(db)
        elif choice == '2':
            user = login(db)
            if user:
                logged_in_menu(db, user)
        elif choice == '3':
            db.close()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def register(db):
    username = input("Enter username: ")
    password = input("Enter password: ")
    user_id = db.create_user(username, password)
    if user_id:
        print(f"User {username} registered successfully.")
    else:
        print(f"Username {username} already exists.")

def login(db):
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = db.get_user_by_username(username)
    if user and user.password == password:
        print(f"Welcome, {user.username}!")
        return user
    else:
        print("Invalid username or password.")
        return None

def logged_in_menu(db, user):
    while True:
        print(f"\n--- Logged in as {user.username} ---")
        print("1. View Menus")
        print("2. Manage Users")
        print("3. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            manage_menus(db)
        elif choice == '2':
            manage_users(db)
        elif choice == '3':
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_menus(db):
    while True:
        print("\n--- Manage Menus ---")
        print("1. View All Menus")
        print("2. Add Menu")
        print("3. Delete Menu")
        print("4. View Menu Items")
        print("5. Add Item to Menu")
        print("6. Delete Item from Menu")
        print("7. Back to Logged In Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            menus = db.get_all_menus()
            if menus:
                for menu in menus:
                    print(f"ID: {menu[0]}, Name: {menu[1]}")
            else:
                print("No menus available.")
        elif choice == '2':
            name = input("Enter menu name: ")
            menu_id = db.create_menu(name)
            if menu_id:
                print(f"Menu '{name}' created with ID {menu_id}.")
            else:
                print(f"Menu with name '{name}' already exists.")
        elif choice == '3':
            menu_id = input("Enter menu ID to delete: ")
            if db.delete_menu(menu_id):
                print(f"Menu with ID {menu_id} deleted successfully.")
            # else:
            #     print(f"Menu with ID {menu_id} does not exist.")
        elif choice == '4':
            menu_id = input("Enter menu ID to view items: ")
            items = db.get_items_in_menu(menu_id)
            if items:
                for item in items:
                    print(f"ID: {item[0]}, Name: {item[2]}, Price: {item[3]}")
            else:
                print(f"No items found for menu ID {menu_id}.")
        elif choice == '5':
            menu_id = input("Enter menu ID to add item to: ")
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            item_id = db.add_item_to_menu(menu_id, name, price)
            if item_id:
                print(f"Item '{name}' added to menu with ID {menu_id}.")
            else:
                print(f"Item '{name}' already exists in menu.")
        elif choice == '6':
            item_id = input("Enter item ID to delete: ")
            if db.delete_item_from_menu(item_id):
                print(f"Item with ID {item_id} deleted successfully.")
            # else:
            #     print(f"Item with ID {item_id} does not exist.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users(db):
    while True:
        print("\n--- Manage Users ---")
        print("1. View All Users")
        print("2. Delete User")
        print("3. Back to Logged In Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user.id}, Username: {user.username}")
            else:
                print("No users available.")
        elif choice == '2':
            user_id = input("Enter user ID to delete: ")
            if db.delete_user(user_id):
                print(f"User with ID {user_id} deleted successfully.")
            else:
                print(f"User with ID {user_id} does not exist.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

# def place_order(db):
#     print("Functionality to place an order is not implemented yet.")

if __name__ == "__main__":
    db = Database('restaurant.db')
    main_menu(db)
