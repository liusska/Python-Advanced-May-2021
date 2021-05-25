n = int(input())

longest_intersection_set = set()

for _ in range(n):
    first, second = input().split('-')

    first_start, first_end = first.split(',')
    first_start = int(first_start)
    first_end = int(first_end)

    first_range_set = set()
    for i in range(int(first_start), int(first_end+1)):
        first_range_set.add(i)

    second_start, second_end = second.split(',')
    second_start = int(second_start)
    second_end = int(second_end)

    second_range_set = set()
    for i in range(second_start, second_end+1):
        second_range_set.add(i)

    current_intersection = first_range_set.intersection(second_range_set)
    if len(current_intersection) > len(longest_intersection_set):
        longest_intersection_set = current_intersection

longest_intersection_set_as_string = ', '.join(f'{x}' for x in longest_intersection_set)

print(f'Longest intersection is [{longest_intersection_set_as_string}] with length {len(longest_intersection_set)}')

