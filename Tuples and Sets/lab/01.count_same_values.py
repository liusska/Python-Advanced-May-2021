nums = tuple([float(x) for x in input().split()])

result = {}

for num in nums:
    if num not in result:
        result[num] = 0
    result[num] += 1


[print(f'{key} - {value} times') for key, value in result.items()]