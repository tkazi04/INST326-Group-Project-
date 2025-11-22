"""
    This file allows users to:
    - Add new tasks
    - List all tasks
    - Complete a task
    - Edit task information
    - Remove a task
    - Search tasks by keyword
    - Save tasks to JSON
    - Load tasks from JSON

It interacts with TaskManager, which manages storage,
searching, filtering, sorting, and persistence of Task objects.
"""

from TaskManager import TaskManager

def print_menu():
    """This is main menu opition for users"""
    print("\n===== Campus Task Organizer =====")
    print("1. Add Task")
    print("2. List All Tasks")
    print("3. Complete Task")
    print("4. Edit Task")
    print("5. Remove Task")
    print("6. Search Tasks")
    print("7. Save Tasks")
    print("8. Load Tasks")
    print("9. Exit")
    print("=================================")
    
