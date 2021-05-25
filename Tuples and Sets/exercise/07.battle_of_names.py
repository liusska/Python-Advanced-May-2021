n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n+1):
    current_value = 0
    name = input()
    for ch in name:
        current_value += ord(ch)
    current_value //= i
    if current_value % 2 == 0:
        even_set.add(current_value)
    else:
        odd_set.add(current_value)

odd_sum = sum(odd_set)
even_sum = sum(even_set)
final_set_for_print = set()

if odd_sum > even_sum:
    final_set_for_print = odd_set.difference(even_set)
else:
    final_set_for_print = odd_set.symmetric_difference(even_set)

print(', '.join([str(x) for x in final_set_for_print]))