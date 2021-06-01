from collections import deque


def check_valid_value(element, type_data):
    if element <= 0:
        if type_data == 'firework' and fireworks:
            element = fireworks.popleft()
            return check_valid_value(element, type_data)
        elif type_data == 'explosive' and explosives:
            element = explosives.pop()
            return check_valid_value(element, type_data)
        return 0
    return element


fireworks = deque(int(x) for x in input().split(', '))
explosives = [int(x) for x in input().split(', ')]
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
successful_show = False

while fireworks and explosives:
    current_fireworks = check_valid_value(fireworks.popleft(), 'firework')
    current_explosives = check_valid_value(explosives.pop(), 'explosive')
    if current_fireworks > 0 and current_explosives > 0:
        total = current_fireworks + current_explosives
        if total % 3 == 0 and not total % 5 == 0:
            palm_fireworks += 1
        elif total % 5 == 0 and not total % 3 == 0:
            willow_fireworks += 1
        elif total % 5 == 0 and total % 3 == 0:
            crossette_fireworks += 1
        else:
            current_fireworks -= 1
            fireworks.append(current_fireworks)
            explosives.append(current_explosives)
        if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
            successful_show = True
            print(f'Congrats! You made the perfect firework show!')
            break
    else:
        if current_fireworks == 0:
            explosives.append(current_explosives)
        if current_explosives == 0:
            fireworks.appendleft(current_fireworks)

if not successful_show:
    print("Sorry. You can’t make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks])}")
if explosives:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosives])}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")