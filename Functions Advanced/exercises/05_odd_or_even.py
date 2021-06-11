def is_even_or_odd(command, nums):
    result = 0
    if command == "Odd":
        new_nums = [x for x in nums if x % 2 != 0]
        result = sum(new_nums) * len(nums)
    elif command == "Even":
        new_nums = [x for x in nums if x % 2 == 0]
        result = sum(new_nums) * len(nums)
    print(result)


even_or_odd = input()
numbers = [int(x) for x in input().split()]

is_even_or_odd(even_or_odd, numbers)