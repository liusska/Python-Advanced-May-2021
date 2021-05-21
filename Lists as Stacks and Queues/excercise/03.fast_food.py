from collections import deque

food_quantity = int(input())
order_quantity = deque(int(x) for x in input().split())
complete = True

print(max(order_quantity))

while food_quantity > 0 and len(order_quantity) > 0:
    current_order = order_quantity.popleft()
    food_quantity -= current_order
    if food_quantity < 0:
        order_quantity.appendleft(current_order)
        complete = False
        break

if complete:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in order_quantity])}")