n = int(input())

matrix = []
primary_diagonal_sum = 0

for row in range(n):
    matrix.append([int(x) for x in input().split()])
    primary_diagonal_sum += matrix[row][row]

print(primary_diagonal_sum)