from functions import get_todos, write_todos
import time

print(time.strftime("%b %d %Y %H:%M"))

while True:
    user_action = input("Type add, show, edit, complete, exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        todos = [todo.strip('\n') for todo in todos]
        show_todos = [print(f"{index+1}-{todo}") for index, todo in enumerate(todos)]

    elif user_action.startswith("edit"):
        try:
            todos = get_todos()

            todo_number_edit = int(user_action[5:]) - 1
            todos[todo_number_edit] = input("Enter a new todo: ") + '\n'

            write_todos(todos)

        except ValueError:
            print("Command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos = get_todos()

            todo_number_complete = int(user_action[9:]) - 1
            # todos.remove(todos[todo_to_complete])
            todos.pop(todo_number_complete)

            write_todos(todos)

        except IndexError:
            print("Todo index out of range.")
            continue

    elif user_action.startswith("clear"):
        todos = get_todos()
        todos.clear()
        write_todos(todos)
        print("List is empty.")

    elif user_action.startswith("exit"):
        break



