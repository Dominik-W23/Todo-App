import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')
add_button = sg.Button("Add")

app_window = sg.Window("To-do App",
                       layout=[[label], [input_box, add_button]],
                       font=('Helvetica', 20))

while True:
    event, value = app_window.read()

    if event == 'Add':
        todos = functions.get_todos()
        todos.append(value['todo'] + '\n')
        functions.write_todos(todos)
    elif event == sg.WIN_CLOSED:
        break

app_window.close()
