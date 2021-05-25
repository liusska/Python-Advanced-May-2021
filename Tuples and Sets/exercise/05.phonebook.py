phonebook = {}

command = input()
while not command[0].isdigit():
    name, number = command.split('-')
    phonebook[name] = number

    command = input()

n = int(command)
for _ in range(n):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')