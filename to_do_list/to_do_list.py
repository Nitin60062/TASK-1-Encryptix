import os

# Function to display the main menu
def display_menu():
    print("\n===== To-Do List Application =====")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

# Function to load tasks from a file
def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:n
            tasks.append(line.strip())
    return tasks

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Function to display tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a new task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added successfully.")

# Function to complete a task
def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_idx = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= task_idx < len(tasks):
            print(f"Completed task: {tasks[task_idx]}")
            tasks.pop(task_idx)
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    else:
        print("No tasks to complete.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_idx < len(tasks):
            print(f"Deleted task: {tasks[task_idx]}")
            tasks.pop(task_idx)
            save_tasks(tasks)
        else:
            print("Invalid task number.")
    else:
        print("No tasks to delete.")

def main():
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
