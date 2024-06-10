from models import User, Task, TimeEntry, Report  
from dbstuff import session
from datetime import datetime

#empty list to keep track of tasks 
tasks = []

# Function to create a new user
def create_user(username, password):
    existing_user = session.query(User).filter_by(username=username).first()
    if existing_user:
        print(f"🖨️ Error: User with username '{username}' already exists.")
        return None

    user = User(username=username, password=password)
    session.add(user)
    session.commit()
    print(f"🖨️ ✅ User {username} created successfully. ✅ ")

    # Create an entry in the reports table to track user creation
    report = Report(user_id=user.user_id, title="User Created", description=f"User {username} was created.")
    session.add(report)
    session.commit()
    return user

# Function to authenticate and return user_id
def login(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        return user.user_id
    else:
        return None

# Function to create a new task
def create_task(user_id, title):
    user = session.query(User).filter_by(user_id=user_id).first()
    if user:
        task = Task(user_id=user_id, title=title)
        session.add(task)
        session.commit()
        tasks.append(task)
        print(f"🖨️ ✅ Task '{title}' created successfully. Task ID: {task.task_id} ✅ ")

        # Create an entry in the time_entries table to track time spent on this task
        time_entry = TimeEntry(user_id=user_id, task_id=task.task_id, start_time=datetime.utcnow())
        session.add(time_entry)
        session.commit()

        # Create an entry in the reports table to track task creation
        report = Report(user_id=user_id, title="Task Created", description=f"Task '{title}' was created.")
        session.add(report)
        session.commit()
    else:
        print(f"🖨️ User with ID '{user_id}' does not exist. Please create a user first.")

# Function to delete tasks by title
def delete_task(username, title):
    user = session.query(User).filter_by(username=username).first()
    if user:
        task_to_delete = session.query(Task).filter_by(user_id=user.user_id, title=title).first()
        if task_to_delete:
            session.delete(task_to_delete)
            session.commit()
            print(f"🖨️ ✅ Task with title '{title}' deleted successfully. ✅ ")
        else:
            print(f"🖨️ No task found with title '{title}' for user '{username}'.")
    else:
        print(f"🖨️ User '{username}' not found.")

# Function to display tasks by username
def display_tasks(username):
    user = session.query(User).filter_by(username=username).first()
    if user:
        tasks = session.query(Task).filter_by(user_id=user.user_id).all()
        if tasks:
            print(f"🖨️ Tasks for {username}:")
            for task in tasks:
                print(f"🖨️ Task ID: {task.task_id}, Title: {task.title}")
        else:
            print(f"🖨️ No tasks found for {username}.")
    else:
        print(f"🖨️ User '{username}' not found.")

# Function to generate a report of users and their tasks
def generate_report():
    users = session.query(User).all()
    print("User Report:")
    for user in users:
        print(f"User: {user.username}")
        tasks = session.query(Task).filter_by(user_id=user.user_id).all()
        for task in tasks:
            print(f"  Task ID: {task.task_id}, Title: {task.title}")

# Function to delete a user and associated tasks
def delete_user(username, password):
    user = session.query(User).filter_by(username=username, password=password).first()
    if user:
        # Delete the user's time entries first
        time_entries = session.query(TimeEntry).filter_by(user_id=user.user_id).all()
        for time_entry in time_entries:
            session.delete(time_entry)

        # Delete the user's reports
        reports = session.query(Report).filter_by(user_id=user.user_id).all()
        for report in reports:
            session.delete(report)

        # Delete the user's tasks
        tasks = session.query(Task).filter_by(user_id=user.user_id).all()
        for task in tasks:
            session.delete(task)

        session.delete(user)
        session.commit()
        print(f"🖨️ User '{username}' and associated tasks, reports, and time entries deleted successfully.")
    else:
        print("🖨️ User not found or password is incorrect.")



if __name__ == '__main__':
    while True:
        print("*********** 💫 Available actions 💫  ************")
        print("1. Create User")
        print("2. Login")
        print("3. Create Task")
        print("4. Delete Task")
        print("5. Display Tasks")
        print("6. Generate Report")
        print("7. Delete a User")
        print("8. Exit")

        choice = input("🗣️ Enter the number of your choice: ")

        if choice == '1':
            username = input("🗣️ Enter username: ")
            password = input("🗣️ Enter password: ")
            create_user(username, password)
        elif choice == '2':
            username = input("🗣️ Enter username: ")
            password = input("🗣️ Enter password: ")
            user_id = login(username, password)
            if user_id:
                print(f" ✅ Login successful. User ID: {user_id} ✅ ")
            else:
                print(" ❌ Login failed. Invalid username or password. ❌ ")
        elif choice == '3':
            username = input("🗣️ Enter your username: ")
            user = session.query(User).filter_by(username=username).first()
            if user:
                title = input("Enter task title: ")
                create_task(user.user_id, title)
            else:
                print(" ❌ User not found. Please create a user first. ❌ ")
        elif choice == '4':
            username = input("🗣️ Enter your username: ")
            user = session.query(User).filter_by(username=username).first()
            if user:
                title = input("🗣️ Enter task title to delete: ")
                delete_task(username, title)
            else:
                print(" ❌ User not found. ❌ ")
        elif choice == '5':
            username = input("🗣️ Enter your username: ")
            display_tasks(username)
        elif choice == '6':
            generate_report()
        elif choice == '7':
            username = input("🗣️ Enter username: ")
            password = input("🗣️ Enter password: ")
            delete_user(username, password)
        elif choice == '8':
            print(" 😘 Goodbye!")
            break