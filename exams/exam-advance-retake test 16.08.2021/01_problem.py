from collections import deque
from functools import reduce


def make_honey(bee, nectar, op):
    data = (bee, nectar)
    if op == "+":
        return reduce(lambda x, y: x+y, data)
    elif op == "-":
        return reduce(lambda x, y: x-y, data)
    elif op == "*":
        return reduce(lambda x, y: x*y, data)
    elif op == "/":
        return reduce(lambda x, y: x/y, data)


def find_match(bee, nectar_data):
    a=5
    if len(nectar_data) > 0:
        value = nectar_data.pop()
        if value >= bee:
            return value
        return find_match(bee, nectar_data)
    return False


working_bees = deque([int(x) for x in input().split()])
nectar_values = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while True:
    if len(working_bees) == 0 or len(nectar_values) == 0:
        break
    bee = working_bees.popleft()
    match = find_match(bee, nectar_values)
    if match:
        action = symbols.popleft()
        honey = make_honey(bee, match, action)
        total_honey += abs(honey)
    else:
        if len(nectar_values) == 0 and bee:
            working_bees.appendleft(bee)
            break

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar_values:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_values])}")