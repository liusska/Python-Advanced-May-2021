from functools import reduce


def operate(*args):
    if args[0] == '*':
        return reduce(lambda x, y: x*y, args[1:])
    elif args[0] == '/':
        return reduce(lambda x, y: x/y, args[1:])
    elif args[0] == '+':
        return reduce(lambda x, y: x+y, args[1:])
    elif args[0] == '-':
        return reduce(lambda x, y: x-y, args[1:])


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))