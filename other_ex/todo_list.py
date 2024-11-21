def display_task(tasks):
    if not tasks:
        print("your list is empty, You do not have any task to complete.")
    else:
        print("your tasks to do are: ")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}.{task}")

def add_tasks(tasks):
    task = input("Enter the task you want to add in your to-do list:")
    tasks.append(task)
    print(f"task {task} is added in your list")

def remove_task(tasks):
    display_task(tasks)
    try:
        task_number = int(input("enter the task number you want to remove:"))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"your task {removed_task} is removed from your to-do list")
        else:
            print("invalid task number")
    except ValueError:
        print("please enter the valid number.")

def to_do_list():
    tasks= []
    while True:
        print("1. View your to-do list tasks")
        print("2. add task to your list")
        print("3. remove task from your list")
        print("4. exit")
        choice = input("enter your choice: ")

        if choice == "1":
            display_task(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting from your to-do list, have a wonderful day")
            break
        else:
            print("invalid choice, please try again..!!")

to_do_list()