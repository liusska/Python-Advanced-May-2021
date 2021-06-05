start_idx = int(input())
end_idx = int(input())

numbers = [x for x in range(start_idx, end_idx+1)]
numbers_to_ten = [x for x in range(2, 11)]

filtered_numbers = [num for num in numbers if any([num % x == 0 for x in numbers_to_ten])]

print(filtered_numbers)
