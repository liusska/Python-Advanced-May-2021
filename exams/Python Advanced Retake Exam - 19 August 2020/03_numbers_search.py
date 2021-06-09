def numbers_searching(*args):
    numbers = [int(x) for x in args]
    sorted_numbers = sorted(numbers)

    duplicate_numbers_as_set = set()
    missing_numbers = []

    for i in range(sorted_numbers[0], sorted_numbers[-1]):
        if i not in numbers:
            missing_numbers.append(i)

    for num in numbers:
        if numbers.count(num) > 1:
            duplicate_numbers_as_set.add(num)

    duplicate_numbers = sorted(list(duplicate_numbers_as_set))
    missing_numbers.append(duplicate_numbers)
    return missing_numbers


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

