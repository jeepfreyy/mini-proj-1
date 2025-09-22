tasks = []


def add_task(task):
    tasks.append(task)
    print("task added!")
    print("\n")


def show_tasks():
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        print("List of Tasks")
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

    print ("\n")


def remove_task(task_number):
    tasks.pop(task_number)
    print("task removed!!")





def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        print("\n")
        choice = input("Enter choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            index = int(input("Enter task number to remove: "))
            remove_task(index)
        elif choice == "4":
            break
        else:
            print("Wrong choice!!")


if __name__ == "__main__":
    main()
