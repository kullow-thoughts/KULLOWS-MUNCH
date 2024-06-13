from database import Database
from models.user import User
from getpass import getpass

def main_menu(db):
    while True:
        print("\nRestaurant Management System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            register_user(db)
        elif choice == '2':
            user = login(db)
            if user:
                logged_in_menu(db, user)
            else:
                print("Login failed. Please try again.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def register_user(db):
    while True:
        username = input("Enter username: ")
        password = getpass("Enter password: ")
        confirm_password = getpass("Confirm password: ")

        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

        # Check if username already exists
        existing_user = db.get_user_by_username(username)
        if existing_user:
            print("Username already exists. Please choose a different username.")
            continue

        # Create new user
        user_id = db.create_user(username, password)
        if user_id:
            print(f"User '{username}' registered successfully!")
            break
        else:
            print("Failed to register user. Please try again.")

def login(db):
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    user = db.get_user_by_username(username)
    if user and user.password == password:
        print(f"Welcome, {user.username}!")
        return user
    else:
        return None

def logged_in_menu(db, user):
    while True:
        print("\nLogged In Menu")
        print("1. Manage Menus")
        print("2. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            manage_menus(db)
        elif choice == '2':
            print(f"Logging out {user.username}...")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_menus(db):
    while True:
        print("\nManage Menus")
        print("1. Create Menu")
        print("2. Delete Menu")
        print("3. Display All Menus")
        print("4. View Items in a Menu")
        print("5. Back to Logged In Menu")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter menu name: ")
            menu_id = db.create_menu(name)
            print(f"Menu '{name}' created with ID {menu_id}.")
        elif choice == '2':
            menu_id = int(input("Enter menu ID to delete: "))
            db.delete_menu(menu_id)
            print(f"Menu with ID {menu_id} deleted.")
        elif choice == '3':
            menus = db.get_all_menus()
            if menus:
                for menu in menus:
                    print(menu)
            else:
                print("No menus found.")
        elif choice == '4':
            menu_id = int(input("Enter menu ID to view items: "))
            items = db.get_items_in_menu(menu_id)
            if items:
                for item in items:
                    print(item)
            else:
                print("No items found in this menu.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    db = Database("food_app.db")
    main_menu(db)
    db.close()
    
if __name__ == "__main__":
    # Your main CLI logic here
    user = User(1, "username", "password")
    print(user)
