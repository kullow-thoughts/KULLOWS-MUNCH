import sqlite3
import getpass

def register():
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Registration successful!")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    
    conn.close()

def login():
    conn = sqlite3.connect('kullows_munch.db')
    cursor = conn.cursor()
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        print("Login successful!")
    else:
        print("Invalid username or password.")
    
    conn.close()
    return user
