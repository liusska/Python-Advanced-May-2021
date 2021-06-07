def round_numbers(data):
    return [round(num) for num in data]


numbers = [float(x) for x in input().split()]

print(round_numbers(numbers))