import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')
list_box = sg.Listbox(values=functions.get_todos(), key='items',
                      enable_events=True, size=(40, 15))

add_button = sg.Button('Add')
edit_button = sg.Button('Edit')

app_window = sg.Window("To-do App",
                       layout=[[label], [input_box, add_button], [list_box, edit_button]],
                       font=('Helvetica', 20))

while True:
    event, value = app_window.read()

    if event == 'Add':
        todos = functions.get_todos()
        todos.append(value['todo'] + '\n')
        functions.write_todos(todos)
        app_window['items'].update(values=todos)
        app_window['todo'].update(value='')

    elif event == 'Edit':
        todos = functions.get_todos()
        todo_to_edit = value['items'][0]
        todo_to_write = value['todo']

        index_to_edit = todos.index(todo_to_edit)
        todos[index_to_edit] = todo_to_write

        functions.write_todos(todos)
        app_window['items'].update(values=todos)

    elif event == 'items':
        app_window['todo'].update(value=value['items'][0])

    elif event == sg.WIN_CLOSED:
        break

    print(event)
    print(value)

app_window.close()
