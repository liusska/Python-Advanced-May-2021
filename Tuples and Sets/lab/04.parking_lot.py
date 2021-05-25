n = int(input())

cars = set()

for _ in range(n):
    command, number = input().split(', ')
    if command == 'IN':
        cars.add(number)
    elif command == 'OUT':
        cars.discard(number)

if not cars:
    print(f'Parking Lot is Empty')
else:
    [print(num) for num in cars]