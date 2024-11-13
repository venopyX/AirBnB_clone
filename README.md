# 🏠 AirBnB Clone Project

![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## 🌟 Project Overview

This project marks the first phase of building a clone of the AirBnB web application. In this stage, we focus on developing a robust backend system integrated with a custom command-line interface (CLI). Using Python's Object-Oriented Programming (OOP) principles, the console application enables users to interact with the backend, storing data as JSON objects.

### 📚 Features of the Command Interpreter:

The interpreter is a simple command-line tool resembling a basic shell interface. It's designed to facilitate user interaction with the application's data models and perform a variety of operations, including:

- Creating, updating, and deleting objects.
- Retrieving data from file storage.
- Counting objects and displaying specific statistics.

### Available Commands:

- `create`
- `show`
- `update`
- `destroy`
- `count`

## 🚀 Getting Started

These steps will guide you to set up the project on your local machine for testing and development purposes.

### 🛠️ Prerequisites

- Python 3.x
- Git

### 💻 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/username/AirBnB_clone.git
   ```
   
2. **Navigate to the Project Directory:**
   ```bash
   cd AirBnB_clone
   ```

3. **Start the Command Interpreter:**
   ```bash
   ./console.py
   ```

## 📝 Project Structure

Here's a brief overview of the main files and folders in the project:

```
AirBnB_clone/
├── AUTHORS
├── README.md
├── console.py
└── models/
    ├── base_model.py
    ├── user.py
    ├── state.py
    ├── city.py
    ├── place.py
    ├── amenity.py
    ├── review.py
    └── engine/
        └── file_storage.py
```

- **`console.py`**: The main command interpreter script.
- **`models/`**: Contains the data models for the project.
- **`engine/`**: Handles file storage and data persistence using JSON.
- **`base_model.py`**: The base class from which other data models inherit.

## 🧑‍💻 Usage

You can use the interpreter in **Interactive** and **Non-Interactive** modes:

### 🔄 Interactive Mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <command>):
========================================
EOF  help  quit  create  show  update  destroy  all  count

(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) quit
$
```

### 🤖 Non-Interactive Mode

You can also pipe commands directly:

```bash
$ echo "create User" | ./console.py
(hbnb) 
$ echo "show User 1234-5678-9012" | ./console.py
(hbnb) 
```

## 🛠️ Command Details

| Command           | Description                                                  | Usage Example                          |
|-------------------|--------------------------------------------------------------|----------------------------------------|
| **`quit`/`EOF`**  | Exits the console.                                           | `(hbnb) quit`                          |
| **`create`**      | Creates a new instance of a model and saves it.              | `(hbnb) create User`                   |
| **`show`**        | Displays the string representation of an instance.           | `(hbnb) show User <id>`                |
| **`destroy`**     | Deletes an instance based on the class name and ID.          | `(hbnb) destroy User <id>`             |
| **`all`**         | Shows all instances of a class or all classes if unspecified.| `(hbnb) all User`                      |
| **`update`**      | Updates an instance by adding/updating attributes.           | `(hbnb) update User <id> <attr> <val>` |
| **`count`**       | Returns the number of instances of a class.                  | `(hbnb) User.count()`                  |

## 🛎️ Examples

Here are some command usage examples:

1. **Create a New User:**
   ```bash
   (hbnb) create User
   1234-5678-9012
   ```

2. **Show User Details:**
   ```bash
   (hbnb) show User 1234-5678-9012
   [User] (1234-5678-9012) {'id': '1234-5678-9012', 'created_at': '2024-11-13T14:48:32'}
   ```

3. **Update User Attribute:**
   ```bash
   (hbnb) update User 1234-5678-9012 name "John Doe"
   ```

4. **Count All Users:**
   ```bash
   (hbnb) User.count()
   5
   ```

## 📃 Authors

- **Gemechis Chala** - [gladsonchala@gmail.com](mailto:gladsonchala@gmail.com)
