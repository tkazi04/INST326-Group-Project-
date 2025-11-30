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
from Course import Course

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
    
def main():
    tm = TaskManager()
    default_course = tm.add_course("General Tasks", "GEN101")
    
    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            due_date = input("Due date (MM-DD-YYYY): ")
            task = tm.add_task(title, due_date)
            default_course.add_task(title, due_date)
            print(f"Task added with ID: {task.id}")

        elif choice == "2":
            print("\n--- All Tasks ---")
            print(tm)

        elif choice == "3":
            task_id = input("Enter Task ID to mark complete: ")
            if tm.complete_task(task_id):
                print("Task marked as completed.")
            else:
                print("Task not found.")

        elif choice == "4":
            task_id = input("Enter Task ID to edit: ")
            new_title = input("New title (leave blank to skip): ")
            new_date = input("New due date MM-DD-YYYY (leave blank to skip): ")
            status = input("Mark completed? (y/n/leave blank): ")

            completed_flag = None
            if status.lower() == "y":
                completed_flag = True
            elif status.lower() == "n":
                completed_flag = False

            success = tm.edit_task(
                task_id,
                title=new_title if new_title else None,
                due_date=new_date if new_date else None,
                completed=completed_flag
            )

            print("Task updated." if success else "Task not found.")

        elif choice == "5":
            task_id = input("Enter Task ID to remove: ")
            if tm.remove_task(task_id):
                print("Task removed.")
            else:
                print("Task not found.")

        elif choice == "6":
            keyword = input("Enter search keyword: ")
            results = tm.search_tasks(keyword)
            print("\n--- Search Results ---")
            if results:
                for t in results:
                    print(t)
            else:
                print("No matching tasks found.")

        elif choice == "7":
            tm.save()
            print("Tasks saved to tasks.json")

        elif choice == "8":
            if tm.load():
                print("Tasks loaded from tasks.json")
            else:
                print("No saved file found.")

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
            
if __name__ == "__main__":
        main()