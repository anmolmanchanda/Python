todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the list.")

def remove_task(task_index):
    if 0 <= task_index < len(todo_list):
        removed_task = todo_list.pop(task_index)
        print(f"Task '{removed_task['task']}' removed from the list.")
    else:
        print("Invalid task number.")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list):
            status = "completed" if task["completed"] else "not completed"
            print(f"{index + 1}. {task['task']} [{status}]")

def mark_task_completed(task_index):
    if 0 <= task_index < len(todo_list):
        todo_list[task_index]["completed"] = True
        print(f"Task '{todo_list[task_index]['task']}' masked as completed.")
    else:
        print("Invalid task number.")

def todo_app():
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input ("Enter the task: ")
            add_task(task)
        elif choice == '2':
            try:
                task_index = int(input("Enter the task number to remove: ")) - 1
                remove_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            try:
                task_index = int(input("Enter the task number to mark as completed: ")) - 1
                mark_task_completed(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            print("Exiting the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    todo_app()