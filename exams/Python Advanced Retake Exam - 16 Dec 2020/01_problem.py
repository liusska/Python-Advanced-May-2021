from collections import deque


def valid_value(value, gender):
    if value <= 0 or value % 25 == 0:
        if gender == 'male':
            if male:
                value = male.pop()
                return valid_value(value, 'male')
            return False
        if gender == 'female':
            if female:
                value = female.popleft()
                return valid_value(value, 'female')
            return False
    return value


male = [int(x) for x in input().split()]
female = deque(int(x) for x in input().split())
matches = 0

while female and male:
    current_male = valid_value(male.pop(), 'male')
    current_female = valid_value(female.popleft(), 'female')
    if current_male and current_female:
        if current_female == current_male:
            matches += 1
        else:
            male.append(current_male - 2)
    else:
        if not current_male:
            female.appendleft(current_female)
        if not current_female:
            male.append(current_male)
        break


print(f'Matches: {matches}')
if male:
    male.reverse()
    print(f"Males left: {(', '.join(str(x) for x in male))}")
else:
    print("Males left: none")
if female:
    print(f"Females left: {', '.join(str(x) for x in female)}")
else:
    print("Females left: none")
