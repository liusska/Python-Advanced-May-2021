from lab.fibonacci_sequence.helper import generate_sequence, find_number

command = input()

while not command == "Stop":
    data = command.split()
    if data[0] == "Create":
        fib_nums = generate_sequence(int(data[-1]))
        print(' '.join([str(x) for x in fib_nums]))
    else:
        result = find_number(int(data[-1]), fib_nums)
        print(result)

    command = input()