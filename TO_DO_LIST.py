tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks added yet!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task['done'] else "Pending"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task: ")
    if title:
        tasks.append({"title": title, "done": False})
        print("Task added.")
    else:
        print("Task cannot be empty.")

def mark_task_done():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to mark as done: "))
            if 0 < task_no <= len(tasks):
                tasks[task_no - 1]['done'] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")

def delete_task():
    show_tasks()
    if tasks:
        try:
            task_no = int(input("Enter task number to delete: "))
            if 0 < task_no <= len(tasks):
                tasks.pop(task_no - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")

def main():
    while True:
        print("\n==== To-Do List Menu ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
