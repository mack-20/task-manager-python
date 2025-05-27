# 📝 Simple Task Manager

A **console-based task management app** built using core Python programming fundamentals. This lightweight tool helps users manage their daily tasks—add, view, mark as done, and delete—right from the terminal.

---

## 🚀 Features

* ✅ **Add New Tasks**
* 👀 **View All Tasks**
* ✔️ **Mark Tasks as Done**
* 🗑️ **Delete Tasks**
* 💾 **Data Persistence (Save & Load from File)**

---

## 🛠️ Built With

* Python `3.x`
* Core programming concepts:

  * Variables
  * Lists
  * Conditionals
  * Loops
  * Functions
  * File I/O
  * JSON serialization

---

## 📂 Project Structure

```
simple-task-manager/
│
├── main.py            # Entry point of the application
├── features.py        # Core task features (add, view, mark done, delete)
├── utils.py           # Utility functions (UI helpers)
├── data.py            # Global task list
└── data.json          # Saved task data (auto-generated)
```

---

## 📦 Installation

> Ensure you have **Python 3.x** installed on your system.

```bash
git clone https://github.com/your-username/simple-task-manager.git
cd simple-task-manager
```

---

## ▶️ Usage

Run the app:

```bash
python main.py
```

Follow the on-screen prompts to manage your tasks:

```
1. Add a new Task
2. View all Tasks
3. Mark a Task as done
4. Delete a Task
5. Exit the app
```

All tasks are saved in `data.json` and automatically loaded when the app starts.

---

## 💡 Example Output

```text
SIMPLE TASK MANAGER
====================
1. Add a new Task
2. View all Tasks
3. Mark a Task as done
4. Delete a Task
5. Exit the app

> 1
Enter task: Buy groceries

Adding task to list...
Task Added with a task id of 0
```

---

## 📌 Notes

* Task IDs are always **even numbers**, as each task is stored with a corresponding completion status in the list.
* Data is persisted between runs using `JSON`.

---

## 📖 License

This project is licensed under the MIT License. Feel free to use and modify it for learning or personal productivity.
