from collections import deque

jobs = [int(x) for x in input().split(', ')]
sorted_jobs = deque(sorted(jobs))
index = int(input())
element = jobs[index]
cycles = 0


for i in range(len(sorted_jobs)):
    current_element = sorted_jobs.popleft()
    current_index = jobs.index(current_element)
    cycles += current_element
    if current_index == index:
        break
    jobs[current_index] = ''

print(cycles)