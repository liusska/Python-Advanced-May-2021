from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pump = [int(x) for x in input().split()]
    pumps.append(pump)

for i in range(n):
    is_valid = True
    fuel = 0

    for _ in range(n):
        current_pump = pumps.popleft()
        fuel += current_pump[0] - current_pump[1]
        if fuel < 0:
            is_valid = False
        pumps.append(current_pump)

        if is_valid:
            print(i)
            break
    pumps.append(pumps.popleft())
