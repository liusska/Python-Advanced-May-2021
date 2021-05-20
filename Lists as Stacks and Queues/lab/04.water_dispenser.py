from collections import deque

queue = deque()

quantity = int(input())

name = input()
while not name == "Start":
    queue.append(name)
    name = input()

command = input()
while not command == "End":
    if command.startswith("refill"):
        refill = int(command.split()[-1])
        quantity += refill
    else:
        needed_quantity = int(command)
        name = queue.popleft()
        if quantity >= needed_quantity:
            quantity -= needed_quantity
            print(f'{name} got water')
        else:
            print(f"{name} must wait")
    command = input()
print(f"{quantity} liters left")