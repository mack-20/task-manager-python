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

from features import *
from utils import *
# ============================================

def main(): 
  # load data
  load_data_from_file()

  # Take user input
  while True:
    try: 
      show_banner()
      show_menu()
      
      user_choice = int(input("> "))

      # Check that user_choice is within range
      if not (user_choice >= 1 and user_choice <= 5):
        raise Exception("ERROR: Enter a value between 1 and 5 only.")
      
      if user_choice == 1:
        add_task()
      elif user_choice == 2:
        view_all_tasks()
      elif user_choice == 3:
        mark_task_as_done()
      elif user_choice == 4:
        delete_task()
      elif user_choice == 5:
        save_data_to_file()
        break
  
    except Exception as E:
      print(E)
  

# Program starts here...
main()
