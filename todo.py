tasks = []


def add_task(task):
    tasks.append(task)
    print("Task added!\n")


def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet\n")
    else:
        print("List of Tasks")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
        print("\n")


def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        tasks.pop(task_number - 1)  # Subtract to match list index
        print("Task removed!!\n")
    else:
        print("Invalid task number!\n")


def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit\n")
        
        choice = input("Enter choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks to remove!\n")
            else:
                index = int(input("Enter task number to remove: "))
                remove_task(index)
        elif choice == "4":
            break
        else:
            print("Wrong choice!!\n")


if __name__ == "__main__":
    main()
