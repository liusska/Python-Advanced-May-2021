heroes = input().split(", ")

items = {hero: [] for hero in heroes}
costs = {hero: 0 for hero in heroes}

while True:
    tokens = input().split("-")
    if tokens[0] == "End":
        break
    name = tokens[0]
    item = tokens[1]
    cost = int(tokens[2])
    if item not in items[name]:
        items[name].append(item)
        costs[name] += cost


for key, value in items.items():
    print(f"{key} -> Items: {len(value)}, Cost: {costs[key]}")