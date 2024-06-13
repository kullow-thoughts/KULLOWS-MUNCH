
  # Restaurant Management CLI Application

## Overview

This Python CLI application is designed to manage a restaurant's menu and provide user authentication functionalities. The application interacts with an SQLite database to store user information, menus.

### Features

- **User Authentication**:
  - Users can register with a username and password.
  - Registered users can log in to access the application.

- **Menu Management**:
  - Create new menus with unique names.
  - Add, view, and delete menu items within each menu.
  - Retrieve all menus and their respective items.

### Technologies Used

- **SQLite**: Database to store user credentials, menus, and menu items.
- **Python 3**: Programming language used for application logic.
- **CLI**: Command-line interface for user interaction.
- **Object-oriented Programming**: Organized code into classes for clear structure and functionality.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- Pip package manager.

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your/repository.git
   cd KULLOWS-MUNCH

<ol start="2">
  <li>Install dependencies using Pipenv:</li>
</ol>

<code>
pipenv install
</code>


## Initialize the SQLite database:
<code>
 python init_db.py
</code>


<p>This command will create the necessary tables (<code>users</code>, <code>menus</code>) in the SQLite database (<code>restaurant.db</code>).</p>

<h2>Usage</h2>

<ol>
  <li>Run the CLI application:</li>
</ol>

<code>
pipenv run python cli.py
</code>

<p><strong>User Management</strong>:</p>

<ol>
  <li>Register: Create a new user account.</li>
  <li>Login: Access the application with your username and password.</li>
</ol>

<p><strong>Menu Management</strong>:</p>

<ol>
  <li>Create Menu: Add a new menu with a unique name.</li>
  <li>View Menu: Display all menus available.</li>
  <li>Add Item to Menu: Include a new food item with its price to a specific menu.</li>
  <li>Delete Menu: Remove a menu from the database, including all associated items.</li>
</ol>

<p><strong>Quit</strong>: Exit the application.</p>

## Contributing

<p>Contributions are welcome! If you'd like to contribute to this project, please fork the repository and submit a pull request with your changes.</p>

## License

<p>This project is licensed under the MIT License - see the [LICENSE] file for details.</p>


