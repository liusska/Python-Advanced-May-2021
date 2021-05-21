numbers = [int(x) for x in input().split()]

reversed_numbers = []

while numbers:
    reversed_numbers.append(numbers.pop())

print(' '.join([str(x) for x in reversed_numbers]))