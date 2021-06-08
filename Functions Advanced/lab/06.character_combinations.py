from itertools import permutations

result = list(permutations(list(input())))

for seq in result:
    print(''.join(seq))