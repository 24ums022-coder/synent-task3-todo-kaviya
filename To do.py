my_tasks = []
while True:
    print("\n1 - Add")
    print("2 - View")
    print("3 - Delete")
    print("4 - Exit")
    option = input("Choose: ")
    if option == "1":
        new_task = input("Enter task: ")
        my_tasks.append(new_task)
        print("Added!")
    elif option == "2":
        if not my_tasks:
            print("No tasks.")
        else:
            for number in range(len(my_tasks)):
                print(number + 1, my_tasks[number])
    elif option == "3":
        if not my_tasks:
            print("No tasks.")
        else:
            number = int(input("Task number: "))

            if 1 <= number <= len(my_tasks):
                my_tasks.pop(number - 1)
                print("Deleted!")
            else:
                print("Invalid number.")
    elif option == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")