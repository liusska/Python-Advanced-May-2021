n = int(input())
all_guests = set()

for _ in range(n):
    all_guests.add(input())

arrived_guests = set()

while True:
    command = input()
    if command == "END":
        break
    arrived_guests.add(command)

not_arrived_guests = all_guests.difference(arrived_guests)

print(len(not_arrived_guests))

vip_guests = set()
regular_guests = set()

for guest in not_arrived_guests:
    if guest[0].isdigit():
        vip_guests.add(guest)
    else:
        regular_guests.add(guest)

all_not_arrived_guests = sorted(vip_guests.union(regular_guests))

[print(guest) for guest in all_not_arrived_guests]