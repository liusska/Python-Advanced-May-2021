from collections import deque


def is_valid_order(num):
    if 0 <= num <= 10:
        return num


orders = deque(int(x) for x in input().split(', '))
capacity = [int(x) for x in input().split(', ')]

total_pizza_made = 0

while orders and capacity:
    order = orders.popleft()
    employee = capacity.pop()
    current_oder = is_valid_order(order)
    if not current_oder:
        capacity.append(employee)
        continue
    else:
        order = current_oder

    if order > employee:
        order = order - employee
        orders.appendleft(order)
        total_pizza_made += employee
    else:
        total_pizza_made += order

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza_made}')
    print(f'Employees: {", ".join([str(x) for x in capacity])}')
else:
    if not capacity and orders:
        print(f'Not all orders are completed.')
        print(f'Orders left: {", ".join([str(x) for x in orders])}')