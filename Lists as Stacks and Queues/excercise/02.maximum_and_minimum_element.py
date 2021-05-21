n = int(input())

numbers = []

for _ in range(n):
    command = input()
    if command.startswith('1'):
        num = int(command.split()[1])
        numbers.append(num)
    elif command == '2':
        if numbers:
            numbers.pop()
    elif command == '3':
        if numbers:
            print(max(numbers))
    elif command == '4':
        if numbers:
            print(min(numbers))

print(', '.join([str(x) for x in reversed(numbers)]))