tasks = []

def add_tasks():
    
    while True:
        user_tasks = input("Enter a task or tasks separated by space: ").lower()
    
        if user_tasks == "":
            print("task can't be empty")
        else:
            break
    
    if user_tasks in tasks:
        print("You added task already")
    else:
        tasks.extend(user_tasks.split())
        print(tasks)
add_tasks()

def display_tasks():
    print("------Your tasks------")
    if not tasks:
        print("No tasks added")
        return
    for task in tasks:
        print(f"*{task}")
display_tasks()

def remove_task():
    task = input("Enter task you want to remove: ")
    if task not in tasks:
        print("Doesn't doesn't exist")
    else:
        tasks.remove(task)
        print(f"You removed {task}")
remove_task()

def task_done():
    task = input("Which task did you complete? ")
    if task not in tasks:
        print("Task not found")
    else:
        


# while True:
#     print("""What would you like to do?
#         1. Remove item
#         2. View tasks
#         3. q to quit""")

#     user_action = input("Enter a choice? ")
#     if user_action == "1":
#         user_removal = input("What would you like to remove? ")
#         tasks.remove(user_removal)
#         print(f"You removed {user_removal}")
#     elif user_action == "2":
#         print("---Your tasks---")
#         for task in tasks:
#             print(f"* {task}")
#     else:
#         user_action.lower()
#         print("Bye bye!")
#         break
