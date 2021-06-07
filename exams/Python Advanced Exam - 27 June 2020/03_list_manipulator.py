def list_manipulator(*args):
    data = args[0]
    action = args[1]
    position = args[2]

    if action == 'remove':
        if position == 'beginning':
            if len(args) > 3:
                return data[args[3]:]
            return data[1:]

        elif position == 'end':
            if len(args) > 3:
                return data[:args[3]-1]
            return data[:-1]

    elif action == 'add':
        new_data = []
        if position == 'beginning':
            for arg in args[3:]:
                new_data.append(arg)
            return new_data + data

        elif position == 'end':
            for arg in args[3:]:
                data.append(arg)
            return data


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
