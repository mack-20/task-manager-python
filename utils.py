from os import system
from data import tasks

def clear_screen():
  system('cls')

def show_banner():
  print("SIMPLE TASK MANAGER")
  print("="*20)

def show_menu():
  print("1. Add a new Task\n" \
  "2. View all Tasks\n" \
  "3. Mark a Task as done\n" \
  "4. Delete a Task\n" \
  "5. Exit the app\n")

def show_task_with_id():
  for task in tasks:
    if isinstance(task, str):
      task_completed = tasks[tasks.index(task) + 1]

      if task_completed:
        print(f"[x] {task}, id: {tasks.index(task)}")
      else:
        print(f"[ ] {task}, id: {tasks.index(task)}")


def show_task_without_id():
  for task in tasks:
    if isinstance(task, str):
      task_completed = tasks[tasks.index(task) + 1]

      if task_completed:
        print(f"[x] {task}")
      else:
        print(f"[ ] {task}")