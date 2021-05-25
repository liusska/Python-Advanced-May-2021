n = int(input())

unique_names = set()

for _ in range(n):
    name = input()
    unique_names.add(name)

[print(name) for name in unique_names]