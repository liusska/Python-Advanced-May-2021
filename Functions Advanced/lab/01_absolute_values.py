def make_absolute(sequence):
    return [abs(el) for el in sequence]


numbers = [abs(float(number)) for number in input().split()]

print(make_absolute(numbers))
