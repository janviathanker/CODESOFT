import os

todo_list = []

def display_menu():
    print("\n====== To-Do List Application ======")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            status = "✔ Completed" if task['completed'] else "✘ Incomplete"
            print(f"{i}. {task['task']} [{status}]")

def add_task():
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        todo_list.append({"task": task_name, "completed": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def update_task():
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to update: "))
            if 1 <= task_number <= len(todo_list):
                new_task_name = input("Enter the updated task: ").strip()
                if new_task_name:
                    todo_list[task_number - 1]["task"] = new_task_name
                    print("Task updated successfully!")
                else:
                    print("Task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"Task '{removed_task['task']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_completed():
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_number <= len(todo_list):
                todo_list[task_number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                update_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                mark_completed()
            elif choice == 6:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()