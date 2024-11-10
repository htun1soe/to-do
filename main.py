from pyfiglet import Figlet
from tabulate import tabulate
import sys


def main():
    figlet = Figlet()
    figlet.getFonts()
    figlet.setFont(font="slant")

    print(figlet.renderText("To Do List App"))

    headers = ["Option", "Action"]
    table = [
        ["V", "View Tasks"],
        ["C", "Create a Task"],
        ["U", "Update a Task"],
        ["D", "Delete a Task"],
        ["P", "Priortize a task"],
        ["E", "Exit"],
    ]

    tasks = []

    while True:
        print(tabulate(table, headers, tablefmt="grid"))
        print()

        choice = input("What do you what to do? ").upper().strip()

        if choice not in ["V", "C", "U", "D", "P", "E"]:
            print("Please choose available options below.")
        elif choice == "V":
            if len(tasks) == 0:
                print("You don't have any tasks yet 😕")
            else:
                print(tabulate(get_usr_tasks(tasks), ["ID", "Task"], tablefmt="grid"))
                print()
        elif choice == "C":
            new_task = input("Task: ")
            tasks = create_task(tasks, new_task)
        elif choice == "U":
            print(tabulate(get_usr_tasks(tasks), ["ID", "Task"], tablefmt="grid"))
            id = int(input("What do you want to update with? "))
            updated_task = input("What do you want to update it to? ")
            tasks = update_task(tasks, id, updated_task)
            print("Your task have updated successfully 😊")
        elif choice == "D":
            print(tabulate(get_usr_tasks(tasks), ["ID", "Task"], tablefmt="grid"))
            task_id = int(input("Which task would you like to delete? "))
            tasks = delete_task(tasks, task_id)
            print("Your tasks have deleted successfully 😊")
        elif choice == "P":
            print(tabulate(get_usr_tasks(tasks), ["ID", "Task"], tablefmt="grid"))
            prioritized_id = int(input("Which task would you like to proiortize? "))
            tasks = prioritize_task(tasks, prioritized_id)
            print("Your task have priortized successfully 😊")
        elif choice == "E":
            sys.exit("Thanks for using our program 🥰")


def get_usr_tasks(tasks):
    usr_tasks = []
    for index, task in enumerate(tasks):
        usr_tasks.append([index + 1, task])
    return usr_tasks


def create_task(tasks, new_task):
    tasks.append(new_task)
    return tasks


def update_task(tasks, id, updated_task):
    for index in range(len(tasks)):
        if (index + 1) == id:
            tasks[index] = updated_task
    return tasks


def delete_task(tasks, task_id):
    del tasks[task_id - 1]
    return tasks


def prioritize_task(tasks, prioritized_id):
    update_tasks = []
    for index, task in enumerate(tasks):
        if (index + 1) == prioritized_id:
            update_tasks.append(task)
            del tasks[index]
            break
    for task in tasks:
        update_tasks.append(task)
    return update_tasks


if __name__ == "__main__":
    main()