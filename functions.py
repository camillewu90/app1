FILEPATH = 'todos.txt'


def read_todos(filename=FILEPATH):
    """ Read a text file and return the list of
    to-do items
    """
    with open(filename) as f:
        todos = f.readlines()
    return todos


def write_todos(content, filename=FILEPATH):
    """ Write the to-do items list in the text file.
    :param content:
    :param filename:
    :return:
    """
    with open(filename, 'w') as f:
        f.writelines(content)


if __name__ == "__main__":
    print('hello')