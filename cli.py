import functions as func
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:].strip()
        if todo == '':
            print("Enter a todo after command add.")
        else:
            todo += '\n'
            todos = func.read_todos()
            todos.append(todo)
            func.write_todos(todos)
    elif user_action.startswith('show'):
        todos = func.read_todos()
        for i, item in enumerate(todos):
            print(f'{i+1}-{item.strip()}')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:].strip())
            number -= 1
            todos = func.read_todos()
            new_todo = input('Enter the new todo: ').strip()
            todos[number] = new_todo + '\n'
            func. write_todos(todos)

        except ValueError:
            print("Please enter a number after edit.")
            continue

        except IndexError:
            print("The number you entered is out of range.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:].strip())
            todos = func.read_todos()
            index = number - 1
            todo_to_remove = todos[index].strip()
            todos.pop(index)
            func.write_todos(todos)
            message = f'Todo {todo_to_remove} is removed from the list.'
            print(message)

        except ValueError as e:
            print("Please enter a number after complete.")
            continue
        except IndexError as e:
            print("The number you entered is out of range.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command not valid.")
print("Bye!")
