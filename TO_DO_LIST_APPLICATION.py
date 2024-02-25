import os
import json
from datetime import datetime, timedelta

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
        return tasks
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['description']} (Priority: {task['priority']}, Due: {task['due_date']}) {'[Completed]' if task['completed'] else ''}")

def add_task(tasks):
    description = input("Enter task description: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    due_date_str = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    tasks.append({
        "description": description,
        "priority": priority,
        "due_date": due_date.strftime("%Y-%m-%d"),
        "completed": False
    })
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(tasks):
    display_tasks(tasks)
    task_index = input("Enter the number of the task to remove: ")

    try:
        task_index = int(task_index) - 1
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['description']}' removed successfully.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def mark_completed(tasks):
    display_tasks(tasks)
    task_index = input("Enter the number of the task to mark as completed: ")

    try:
        task_index = int(task_index) - 1
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['description']}' marked as completed.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()


