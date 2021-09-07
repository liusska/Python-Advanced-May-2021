from collections import deque


def valid_value(value, ingredient):
    if value <= 0:
        if ingredient == 'milk':
            if milk:
                value = milk.popleft()
                return valid_value(value, 'milk')
            return False
        elif ingredient == 'chocolate':
            if chocolate:
                value = chocolate.pop()
                return valid_value(value, 'chocolate')
            return False
    return value


chocolate = [int(x) for x in input().split(', ')]
milk = deque(int(x) for x in input().split(', '))

chocolate_milkshakes = 0

while chocolate and milk:
    current_chocolate = valid_value(chocolate.pop(), 'chocolate')
    current_milk = valid_value(milk.popleft(), 'milk')
    if current_milk > 0 and current_chocolate > 0:
        if current_milk == current_chocolate:
            chocolate_milkshakes += 1
            if chocolate_milkshakes >= 5:
                break
        else:
            chocolate.append(current_chocolate - 5)
            milk.append(current_milk)
    else:
        if not current_milk and current_chocolate:
            chocolate.append(current_chocolate)
        if not current_chocolate and current_milk:
            milk.appendleft(current_milk)
        break

if chocolate_milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk: empty")
