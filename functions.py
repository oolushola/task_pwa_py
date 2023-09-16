# Todos application using file system operation
FILEPATH = "todo.txt"
def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as readfile:
        return readfile.readlines()


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as writefile:
        writefile.writelines(todos_arg)