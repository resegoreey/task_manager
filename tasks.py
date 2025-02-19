tasks = []
user_tasks = input("Enter a task (q to quit): ")

while True:
    if user_tasks.lower() == "q":
        print("Bye bye!")
        break
   
    else:
        if user_tasks == "":
            print("task can't be empty")
        else:
            tasks.append(user_tasks)
        user_tasks = input("Enter a task (q to quit): ")
print(tasks)