tasks=[]
while True:
    user_input=input("Welcome to your task Manager! Please choose from our menu your next action: (A) Add a task,"
" (B) See all the tasks, (C) Remove a task, (Q) Quit")
    user_input=user_input.upper()
    if user_input=="A":
        add_task=input("Please enter your tasks that you would like to add: ")
        tasks.append(add_task)
        print(tasks)
    elif user_input=="B":
        print(tasks)
    elif user_input=="C":
        remove_task=input("Please enter the task that you would like to remove: ")
        if remove_task in tasks:
            tasks.remove(remove_task)
            print(tasks)
        else:
            print("Sorry! That task doesn't exist! Try again ")
            remove_task=input("Please enter the task to remove ")
    elif user_input=="Q":
        break
