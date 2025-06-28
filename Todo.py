def Todo():
    print('''
          1) List of task remaining
          2) Add a new task
          3) A task that is done
          4) Clear the list
          5) Exit
''')
    Todo_list = []
    #conditions
    while True:
        user_input = int(input("Enter the number from the Menu: "))
        if user_input == 1:
            for i in Todo_list:
                print(i)
        elif user_input == 2:
            user_input_add = input("Enter the new task: ")
            Todo_list.append(user_input_add)
            print("Your Task is added")
        elif user_input == 3:
            for j in Todo_list:
                print(j)
            print("Enter the name of the Task")
            user_input_remove = input()
            Todo_list.remove(user_input_remove)
            print("Task is removed from the list")
        elif user_input == 4:
            Todo_list.clear()
            print("The list has been cleared")
        elif user_input == 5:
            break
    print("You are out from the list")

Todo()