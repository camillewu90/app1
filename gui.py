import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todos = functions.read_todos()
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0].strip())
        case "Complete":
            todo_to_complete = values["todo"] + "\n"
            todos = functions.read_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todo'].update(value="")
            window['todos'].update(values=todos)
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()


