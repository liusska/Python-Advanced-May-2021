numbers = [int(x) for x in input().split(', ')]

positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if not num % 2 == 0]

print(f"Positive: {', '.join([str(x) for x in positive_numbers])}")
print(f"Negative: {', '.join([str(x) for x in negative_numbers])}")
print(f"Even: {', '.join([str(x) for x in even_numbers])}")
print(f"Odd: {', '.join([str(x) for x in odd_numbers])}")