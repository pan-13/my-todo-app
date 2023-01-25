FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and returns a list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        list_todos = file_local.readlines()
    return list_todos


def set_todos(list_todo, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(list_todo)


def count(phrase):
    return phrase.count(".")


if __name__ == "__main__":
    print(get_todos())
