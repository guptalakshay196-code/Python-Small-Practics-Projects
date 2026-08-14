"""
To-Do List Application

Description:
A simple command-line To-Do List application built using Python.
Users can:
- Add new tasks
- View all tasks
- Exit the application

Concepts Used:
- Lists
- Loops (while, for)
- Conditional Statements
- User Input
- enumerate()
- append()
"""
tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("Thank you for using the To-Do List App!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")