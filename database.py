import sqlite3
from models.user import User

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menus (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                menu_id INTEGER,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                FOREIGN KEY (menu_id) REFERENCES menus(id)
            )
        """)
        self.conn.commit()

    def execute_query(self, query, args=None):
        cursor = self.conn.cursor()
        if args:
            cursor.execute(query, args)
        else:
            cursor.execute(query)
        return cursor

    # User-related methods

    def create_user(self, username, password):
        try:
            cursor = self.execute_query("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None  # Username already exists

    def get_user_by_username(self, username):
        cursor = self.execute_query("SELECT * FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        if row:
            return User(id=row[0], username=row[1], password=row[2])
        else:
            return None

    def get_all_users(self):
        cursor = self.execute_query("SELECT * FROM users")
        rows = cursor.fetchall()
        return [User(id=row[0], username=row[1], password=row[2]) for row in rows]

    def delete_user(self, user_id):
        try:
            cursor = self.execute_query("DELETE FROM users WHERE id=?", (user_id,))
            self.conn.commit()
            print(f"User with ID {user_id} deleted successfully.")
        except sqlite3.IntegrityError:
            print(f"Error deleting user with ID {user_id}.")
        finally:
            cursor.close()

    # Menu-related methods

    def create_menu(self, name):
        try:
            cursor = self.execute_query("INSERT INTO menus (name) VALUES (?)", (name,))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Menu with name '{name}' already exists.")
            return None

    def get_menu(self, menu_id):
        cursor = self.execute_query("SELECT * FROM menus WHERE id=?", (menu_id,))
        return cursor.fetchone()

    def get_all_menus(self):
        cursor = self.execute_query("SELECT * FROM menus")
        return cursor.fetchall()

    def delete_menu(self, menu_id):
        try:
            cursor = self.execute_query("DELETE FROM menus WHERE id=?", (menu_id,))
            self.conn.commit()
            print(f"Menu with ID {menu_id} deleted successfully.")
        except sqlite3.IntegrityError:
            print(f"Error deleting menu with ID {menu_id}.")
        finally:
            cursor.close()

    def get_items_in_menu(self, menu_id):
        try:
            cursor = self.execute_query("SELECT * FROM menu_items WHERE menu_id=?", (menu_id,))
            items = cursor.fetchall()

            if items:
                return items
            else:
                print(f"No items found for menu_id: {menu_id}")
                return []

        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def add_item_to_menu(self, menu_id, name, price):
        try:
            cursor = self.execute_query("INSERT INTO menu_items (menu_id, name, price) VALUES (?, ?, ?)", (menu_id, name, price))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            print(f"Item '{name}' already exists in menu.")
            return None

    def delete_item_from_menu(self, item_id):
        try:
            cursor = self.execute_query("DELETE FROM menu_items WHERE id=?", (item_id,))
            self.conn.commit()
            print(f"Item with ID {item_id} deleted successfully.")
        except sqlite3.IntegrityError:
            print(f"Error deleting item with ID {item_id}.")
        finally:
            cursor.close()

    def close(self):
        self.conn.close()
