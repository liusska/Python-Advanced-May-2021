import os


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


def replace_content(file_name, old_content, new_content):
    try:
        with open(file_name, "r+") as file:
            text = ''.join(file.readlines())
            replaced = text.replace(old_content, new_content)
            file.seek(0)
            file.write(replaced)
    except FileNotFoundError:
        print("An error occurred")


def add_content(file_name, content):
    if os.path.exists(file_name):
        with open(file_name, "a") as file:
            file.write(content + '\n')
    else:
        with open(file_name, "w") as file:
            file.write(content)


def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("")


while True:
    action = input()
    if action == "End":
        break
    command = action.split("-")
    if command[0] == "Create":
        create_file(command[1])
    elif command[0] == "Add":
        add_content(command[1], command[2])
    elif command[0] == "Replace":
        replace_content(command[1], command[2], command[3])
    elif command[0] == "Delete":
        delete_file(command[1])
