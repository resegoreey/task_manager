tasks = []
user_tasks = input("Enter a task (q to quit): ")

while True:
    if user_tasks.lower() == "q":
        print("You stopped adding tasks")
        break
   
    else:
        if user_tasks == "":
            print("task can't be empty")
        else:
            tasks.append(user_tasks)
        user_tasks = input("Enter a task (q to quit): ")
print()

while True:
    print("""What would you like to do?
        1. Remove item
        2. View tasks
        3. q to quit""")

    user_action = input("Enter a choice? ")
    if user_action == "1":
        user_removal = input("What would you like to remove? ")
        tasks.remove(user_removal)
        print(f"You removed {user_removal}")
    elif user_action == "2":
        print("---Your tasks---")
        for task in tasks:
            print(f"* {task}")
    else:
        user_action.lower()
        print("Bye bye!")
        break
