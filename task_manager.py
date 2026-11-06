
from datetime import date, datetime


# ==== Login Section ====

users = {}

user_file = open("user.txt", "r")

for line in user_file:
    username, password = line.strip().split(", ")
    users[username] = password

user_file.close()


while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Please try again.")

# ===== Function definitions ====

def reg_user():

    new_username = input("Enter a new username: ")

    if new_username in users:
        print("Username already exists. Please choose a different username.")

    else:
        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm your password: ")

        if new_password == confirm_password:
            user_file = open("user.txt", "a")
            user_file.write(new_username + ", " + new_password + "\n")
            user_file.close()

            # Add the new user to the dictionary
            users[new_username] = new_password
            print("New user registered successfully.")

        else:
            print("Passwords do not match.")
    # registration code


def add_task():

    while True:
        task_username = input(
            "Enter the username of the person the task is assigned to: "
        )

        if task_username in users:
            break

        print(
            "Username not found. Please enter a registered username."
        )

    task_title = input("Enter the title of the task: ")

    task_description = input(
        "Enter the description of the task: "
    )

    while True:
        task_due_date = input(
            "Enter the due date of the task (e.g. 25 Oct 2026): "
        )

        try:
            datetime.strptime(task_due_date, "%d %b %Y")
            break

        except ValueError:
            print(
                "Invalid date. Please use the format DD Mon YYYY, "
                "for example 25 Oct 2026."
            )

    current_date = date.today()

    completed = "No"

    task_file = open("tasks.txt", "a")

    task_file.write(
        task_username + ", " +
        task_title + ", " +
        task_description + ", " +
        str(current_date) + ", " +
        task_due_date + ", " +
        completed + "\n"
    )

    task_file.close()

    print("Task added successfully.")
    # add task code


def view_all():

    task_file = open("tasks.txt", "r")

    for line in task_file:

        task = line.strip().split(", ")

        print()
        print("Task:", task[1])
        print("Assigned to:", task[0])
        print("Date assigned:", task[3])
        print("Due date:", task[4])
        print("Task complete:", task[5])
        print("Task description:", task[2])
        print()

    task_file.close()
    # view all tasks code


def view_mine():

    # Read all tasks
    task_file = open("tasks.txt", "r")
    tasks = task_file.readlines()
    task_file.close()

    # Store only tasks assigned to the logged-in user
    my_tasks = []

    for line in tasks:

        task = line.strip().split(", ")

        if task[0] == username:
            my_tasks.append(task)

    # Check whether the user has any tasks
    if len(my_tasks) == 0:
        print("You have no tasks assigned to you.")
        return

    # Display the user's tasks with numbers
    print()
    print("Your tasks:")

    for i in range(len(my_tasks)):
        print()
        print("Task number:", i + 1)
        print("Task:", my_tasks[i][1])
        print("Assigned to:", my_tasks[i][0])
        print("Date assigned:", my_tasks[i][3])
        print("Due date:", my_tasks[i][4])
        print("Task complete:", my_tasks[i][5])
        print("Task description:", my_tasks[i][2])

    print("-1 - Return to main menu")

    # Allow the user to select a task
    while True:

        try:
            task_number = int(
                input("Enter the number of the task you want to view: ")
            )
        except ValueError:
            print("Please enter a valid task number.")
            continue

        # Return to main menu
        if task_number == -1:
            return

        # Check that the selected task exists
        if task_number < 1 or task_number > len(my_tasks):
            print("Invalid task number. Please try again.")
            continue

        # Get the selected task
        selected_task = my_tasks[task_number - 1]

        print()
        print("Task:", selected_task[1])
        print("Assigned to:", selected_task[0])
        print("Date assigned:", selected_task[3])
        print("Due date:", selected_task[4])
        print("Task complete:", selected_task[5])
        print("Task description:", selected_task[2])
        print()

        # Give the user options for the selected task
        while True:

            print("Please select an option:")
            print("c - Mark task as complete")
            print("e - Edit task")
            print("-1 - Return to main menu")

            option = input(": ").lower()

            if option == "-1":
                return

            elif option == "c":

                # A completed task cannot be marked complete again
                if selected_task[5] == "Yes":
                    print("This task has already been completed.")

                else:
                    selected_task[5] = "Yes"

                    # Update the original task in the tasks list
                    for i in range(len(tasks)):

                        task = tasks[i].strip().split(", ")

                        if (
                            task[0] == selected_task[0]
                            and task[1] == selected_task[1]
                            and task[3] == selected_task[3]
                        ):
                            tasks[i] = (
                                selected_task[0] + ", " +
                                selected_task[1] + ", " +
                                selected_task[2] + ", " +
                                selected_task[3] + ", " +
                                selected_task[4] + ", " +
                                selected_task[5] + "\n"
                            )

                            break

                    # Rewrite tasks.txt
                    task_file = open("tasks.txt", "w")

                    for task in tasks:
                        task_file.write(task)

                    task_file.close()

                    print("Task marked as complete.")

                break

            elif option == "e":

                # Completed tasks cannot be edited
                if selected_task[5] == "Yes":
                    print("Completed tasks cannot be edited.")

                else:

                    print()
                    print("What would you like to edit?")
                    print("u - Change the username")
                    print("d - Change the due date")
                    print("-1 - Cancel")

                    edit_option = input(": ").lower()

                    if edit_option == "u":

                        new_username = input(
                            "Enter the new username: "
                        )

                        if new_username not in users:
                            print("That username does not exist.")

                        else:
                            selected_task[0] = new_username
                            print("Username updated successfully.")

                    elif edit_option == "d":

                        new_due_date = input(
                            "Enter the new due date: "
                        )

                        selected_task[4] = new_due_date
                        print("Due date updated successfully.")

                    elif edit_option == "-1":
                        break

                    else:
                        print("Invalid option.")

                    # Update the task in tasks.txt
                    for i in range(len(tasks)):

                        task = tasks[i].strip().split(", ")

                        if (
                            task[1] == selected_task[1]
                            and task[3] == selected_task[3]
                        ):
                            tasks[i] = (
                                selected_task[0] + ", " +
                                selected_task[1] + ", " +
                                selected_task[2] + ", " +
                                selected_task[3] + ", " +
                                selected_task[4] + ", " +
                                selected_task[5] + "\n"
                            )

                            break

                    task_file = open("tasks.txt", "w")

                    for task in tasks:
                        task_file.write(task)

                    task_file.close()

                break

            else:
                print("Invalid option. Please try again.")


def view_completed():

    found_task = False

    task_file = open("tasks.txt", "r")

    for line in task_file:

        task = line.strip().split(", ")

        if task[5] == "Yes":

            found_task = True

            print()
            print("Task:", task[1])
            print("Assigned to:", task[0])
            print("Date assigned:", task[3])
            print("Due date:", task[4])
            print("Task complete:", task[5])
            print("Task description:", task[2])
            print()

    task_file.close()

    if found_task == False:
        print("No completed tasks are currently available.")
    # view completed tasks code


def delete_task():

    task_file = open("tasks.txt", "r")

    tasks = task_file.readlines()

    task_file.close()

    for i in range(len(tasks)):

        task = tasks[i].strip().split(", ")

        print(i + 1, "-", task[1])

    try:
        task_number = int(
            input("Enter the number of the task you want to delete: ")
    )

    except ValueError:
        print("Invalid input. Please enter a task number.")
        return

    if task_number >= 1 and task_number <= len(tasks):

        del tasks[task_number - 1]

        task_file = open("tasks.txt", "w")

        for task in tasks:
            task_file.write(task)

        task_file.close()

        print("Task deleted successfully.")

    else:
        print("Invalid task number.")
    # delete task code


def generate_reports():

    # Open the tasks file
    task_file = open("tasks.txt", "r")

    tasks = task_file.readlines()

    task_file.close()

    # Calculate the total number of tasks
    total_tasks = len(tasks)

    # Calculate the number of completed tasks
    completed_tasks = 0

    # Calculate the number of incomplete tasks
    incomplete_tasks = 0

    # Calculate the number of incomplete tasks
    overdue_tasks = 0

    for line in tasks:

        task = line.strip().split(", ")

        if task[5] == "Yes":
            completed_tasks += 1

        else:
            incomplete_tasks += 1

            due_date = datetime.strptime(task[4], "%d %b %Y").date()

            if due_date < date.today():
                overdue_tasks +=1

    # Calculate the percentage of incomplete tasks
    if total_tasks > 0:
        incomplete_percentage = (incomplete_tasks / total_tasks) * 100

        overdue_percentage = (overdue_tasks / total_tasks) * 100

    else:
        incomplete_percentage = 0
        overdue_percentage = 0

    # Create the task overview file
    overview_file = open("task_overview.txt", "w")

    overview_file.write(
        "Total number of tasks: " + str(total_tasks) + "\n"
    )

    overview_file.write(
        "Total number of completed tasks: " + str(completed_tasks) + "\n"
    )

    overview_file.write(
        "Total number of incomplete tasks: " + str(incomplete_tasks) + "\n"
    )

    overview_file.write(
        "Percentage of incomplete tasks: " +
        str(incomplete_percentage) + "%\n"
    )

    overview_file.write(
    "Total number of overdue tasks: " + str(overdue_tasks) + "\n"
    )

    overview_file.write(
    "Percentage of overdue tasks: " +
    str(overdue_percentage) + "%\n"
    )
    
    overview_file.close()

    # Calculate the total number of registered users
    total_users = len(users)

    # Create the user overview file
    user_overview_file = open("user_overview.txt", "w")

    user_overview_file.write(
        "Total number of registered users: " + str(total_users) + "\n"
    )

    user_overview_file.write(
        "Total number of tasks: " + str(total_tasks) + "\n"
    )

    # Calculate the number of tasks assigned to each user
    for user in users:

        user_tasks = 0
        user_completed_tasks = 0
        user_incomplete_tasks = 0
        user_overdue_tasks = 0

        for line in tasks:

            task = line.strip().split(", ")

            if task[0] == user:
                user_tasks += 1

                if task[5] == "Yes":
                    user_completed_tasks += 1

                else:
                    user_incomplete_tasks += 1

                    due_date = datetime.strptime(
                        task[4], "%d %b %Y"
                    ).date()

                    if due_date < date.today():
                        user_overdue_tasks += 1

        if total_tasks > 0:
            user_task_percentage = (user_tasks / total_tasks) * 100
        else:
            user_task_percentage = 0

        if user_tasks > 0:
            user_completed_percentage = (
                user_completed_tasks / user_tasks
            ) * 100
            user_incomplete_percentage = (
                user_incomplete_tasks / user_tasks
            ) * 100
            user_overdue_percentage = (
                user_overdue_tasks / user_tasks
            ) * 100
        else:
            user_completed_percentage = 0
            user_incomplete_percentage = 0
            user_overdue_percentage = 0

        user_overview_file.write(
            "\nUser: " + user + "\n"
        )

        user_overview_file.write(
            "Total tasks assigned: " + str(user_tasks) + "\n"
        )

        user_overview_file.write(
            "Percentage of total tasks assigned: " +
            str(user_task_percentage) + "%\n"
        )

        user_overview_file.write(
            "Percentage of assigned tasks completed: " +
            str(user_completed_percentage) + "%\n"
        )

        user_overview_file.write(
            "Percentage of assigned tasks incomplete: " +
            str(user_incomplete_percentage) + "%\n"
        )

        user_overview_file.write(
            "Percentage of assigned tasks overdue: " +
            str(user_overdue_percentage) + "%\n"
        )

    user_overview_file.close()

    
def display_statistics():

    try:
        task_overview_file = open("task_overview.txt", "r")
        user_overview_file = open("user_overview.txt", "r")

    except FileNotFoundError:
        generate_reports()

        task_overview_file = open("task_overview.txt", "r")
        user_overview_file = open("user_overview.txt", "r")

    print("\nTASK OVERVIEW")
    print("-" * 40)

    print(task_overview_file.read())

    print("\nUSER OVERVIEW")
    print("-" * 40)

    print(user_overview_file.read())  

# ==== Main Menu Section ====

while True:
    # Display different menu options depending on whether the user is the admin
    # make sure that the user input is converted to lower case.
    if username == "admin":
        menu = input(
            '''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    vc - view completed tasks
    del - delete a task
    ds - display statistics
    gr - generate reports
    e - exit
    : '''
        ).lower()

    else:
        menu = input(
        '''Please select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : '''
    ).lower()   

    def reg_user():

        new_username = input("Enter a new username: ")

        if new_username in users:
            print("Username already exists. Please choose a different username.")

        else:
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm your password: ")

            if new_password == confirm_password:
                user_file = open("user.txt", "a")
                user_file.write(new_username + ", " + new_password + "\n")
                user_file.close()

                # Add the new user to the dictionary
                users[new_username] = new_password
                print("New user registered successfully.")

            else:
                    print("Passwords do not match.")

    if menu == 'r':

        if username == "admin":
            reg_user()
      
        else:
            print("Only the admin user can register new users.")

    elif menu == 'a':

        add_task()
    
    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'vc':
        view_completed()

    elif menu == 'del':

        if username == "admin":
            delete_task()

        else:
            print("Only the admin user can delete tasks.")
    elif menu == 'gr':

        if username == "admin":
            generate_reports()

        else:
            print("Only the admin user can generate reports.")

    elif menu == 'ds':

        if username == "admin":
            display_statistics()

        else:
            print("Only the admin user can display statistics.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")