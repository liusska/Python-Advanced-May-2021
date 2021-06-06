categories = input().split(", ")
n = int(input())
dict_of_categories = {category: [] for category in categories}
qualities = []
quantities = 0
for _ in range(n):
    category, food, others = input().split(" - ")
    dict_of_categories[category].append(food)

    quantity, quality = others.split(";")
    tokens = quantity.split(":")
    tokens2 = quality.split(":")
    quantities += int(tokens[1])
    qualities.append(int(tokens2[1]))

print(f"Count of items: {quantities}")
print(f"Average quality: {sum(qualities) / len(dict_of_categories):.2f}")

for key, value in dict_of_categories.items():
    print(f"{key} -> {', '.join(value)}")