# ============================================
#            SIMPLE TASK MANAGER
# --------------------------------------------
# A console-based app to manage daily tasks.
# 
# 📌 Features:
# - Add a new task
# - View all tasks
# - Mark a task as done
# - Delete a task
# - Exit the app
# 
# 🛠️ Built using core Python fundamentals:
# Variables, lists, loops, conditionals, and functions
# ============================================

from os import system # to be able to clear screen using 'cls'
from time import sleep

# Global tasks list to hold task and its status
tasks = []

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
  
def add_task():
  # input check
  while True:
    try:
      task = input("Enter task: ").strip()
  
      if not task:
        raise Exception("Input cannot be empty. Try again")
  
      # Valid input, break loop
      break
    except Exception as E:
      print(E)
  
  # add task
  tasks.append(task)

  # add task status
  task_completed = False
  tasks.append(task_completed)

  # animation
  print(f"\nAdding task to list...")
  sleep(1)

  print(f"\nTask Added with a task id of {tasks.index(task)}")
  input("\n\nPress Enter↩ to return to main menu...")

  # clear screen
  clear_screen()

  return

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

def view_all_tasks():
  clear_screen()

  # show header
  print("TASKS")
  print("="*10)

  # display tasks without id
  show_task_without_id()

  # hold this screen till return
  input("\n\nPress Enter↩ to return to main menu...")
  clear_screen()
  return

def mark_task_as_done():
  clear_screen()
  
  # show header
  print("TASKS")
  print("="*10)
  
  # display tasks with id
  show_task_with_id()

  # enter task id to mark as done
  while True:
    try:
      task_id = int(input("\n\nEnter id of task to mark as done: "))

      # if input is not even, wrong id entered
      if not (task_id % 2 == 0):
        raise Exception("Invalid Task ID. Try Again")
      
      # Valid input, break loop
      break
    except Exception as E:
      print(E)


  # pop out task and its status from list
  task_status_index = task_id + 1
  tasks[task_status_index] = True

  # animation
  print("\nMarking task as Done...")
  sleep(1)
  print("\nTask Marked as Done")

  input("\n\nPress Enter↩ to return to main menu...")
  clear_screen()
  return

def delete_task():
  clear_screen()
  
  # show header
  print("TASKS")
  print("="*10)
  
  # display tasks with id
  show_task_with_id()

  # enter task id to mark as done
  while True:
    try:
      task_id = int(input("\n\nEnter id of task to mark as done: "))

      # if input is not even, wrong id entered
      if not (task_id % 2 == 0):
        raise Exception("Invalid Task ID. Try Again")
      
      # Valid input, break loop
      break
    except Exception as E:
      print(E)


  # pop out task and its status from list
  # since after popping the task the list changes, the task 
  # status will now be at the id of the task and not the +1 id
  tasks.pop(task_id) # pops task
  tasks.pop(task_id) # pops task completion status

  # animation
  print("\nDeleting task...")
  sleep(1)
  print("\nTask Deleted")

  input("\n\nPress Enter↩ to return to main menu...")
  clear_screen()
  return

def main(): 
  show_banner()
  show_menu()

  # Take user input
  while True:
    try: 
      user_choice = int(input("> "))

      # Check that user_choice is within range
      if not (user_choice >= 1 and user_choice <= 5):
        raise Exception("ERROR: Enter a value between 1 and 5 only.")
  
      # Valid input, break loop
      break
    except Exception as E:
      print(E)

  if user_choice == 1:
    add_task()
  elif user_choice == 2:
    view_all_tasks()
  elif user_choice == 3:
    mark_task_as_done()
  elif user_choice == 4:
    delete_task()
  elif user_choice == 5:
    exit()
  

# Program starts here...
while True:
  main()
