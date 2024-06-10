from menu import display_menu
from order import place_order, view_order_summary
from user import register, login
from admin import admin_menu

def main():
    user = None
    while True:
        print("\nKullow's Munch")
        if user:
            print(f"Logged in as {user[1]}")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Order Summary")
        print("4. Register")
        print("5. Login")
        print("6. Admin Menu")
        print("7. Logout")
        print("8. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            display_menu()
        elif choice == '2':
            if user:
                display_menu()
                place_order(user)
            else:
                print("You need to log in first.")
        elif choice == '3':
            if user:
                view_order_summary(user)
            else:
                print("You need to log in first.")
        elif choice == '4':
            register()
        elif choice == '5':
            user = login()
        elif choice == '6':
            admin_menu()
        elif choice == '7':
            user = None
            print("Logged out.")
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
