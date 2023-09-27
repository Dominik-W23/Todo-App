FILEPATH = 'todos.txt'
def get_todos(filename=FILEPATH):
    with open(filename) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(content, filename=FILEPATH):
    with open(filename, 'w') as file_local:
        file_local.writelines(content)

