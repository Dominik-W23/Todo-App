import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

app_window = sg.Window("To-do App",
                       layout=[[label], [input_box, add_button]])

app_window.read()
app_window.close()
