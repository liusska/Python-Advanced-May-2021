clothes_for_store = [int(x) for x in input().split()]
capacity = int(input())
current_capacity = capacity
rack = 1

while clothes_for_store:
    clothes = clothes_for_store.pop()
    if current_capacity < clothes:
        rack += 1
        current_capacity = capacity
    current_capacity -= clothes

print(rack)