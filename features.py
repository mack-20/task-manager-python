from utils import show_task_with_id, show_task_without_id, clear_screen
from time import sleep
from data import tasks
 
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