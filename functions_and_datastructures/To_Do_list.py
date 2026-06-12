tasks = []
def add_task():
    task = input("enter the task : ")
    tasks.append(task)
    print(tasks)
def show_tasks():
    for task in tasks:
        print(task)
def remove_task():
    show_tasks()
    task = input("which task to remove : ")
    tasks.remove(task)
    print(tasks)
while True:
    print("\n1.Add task")
    print("2.Show task")
    print("3.Remove task")
    print("4.Exit Task")

    choice = int(input("enter choice : "))
    if choice == 1:
        print(add_task())
    elif choice == 2:
        print(show_tasks())
    elif choice == 3:
        print(remove_task())
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("Invalid Choice")
        
