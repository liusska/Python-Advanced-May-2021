def even_odd(*args):
    data = args[:-1]
    if args[-1] == 'even':
        data = [int(x) for x in data if x % 2 == 0]
    else:
        data = [int(x) for x in data if not x % 2 == 0]
    return data


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
