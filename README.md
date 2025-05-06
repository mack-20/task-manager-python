# 📝 Simple Task Manager

A **console-based Python application** for managing daily tasks.  
Built entirely with **Python fundamentals** — no external libraries, no file handling.

---

## 📌 Features

- ✅ Add a new task  
- 📋 View all tasks  
- ✔️ Mark a task as done  
- ❌ Delete a task  
- 🚪 Exit the app  

---

## ⚙️ Technologies & Concepts Used

- Python built-ins only (`input()`, `print()`, `lists`, `functions`, etc.)
- `os.system('cls')` for clearing screen (Windows only)
- `time.sleep()` for delay effects
- Basic error handling with `try-except`
- Console UI for user interaction

---

## 🧠 How It Works

- Each **task** is stored in a list as a string, followed by its **completion status** (`True` or `False`).
- Example list structure:
  ```python
  ["Buy milk", False, "Read book", True]
