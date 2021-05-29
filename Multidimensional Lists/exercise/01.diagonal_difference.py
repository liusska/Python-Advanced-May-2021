n = int(input())

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

matrix = []

for row in range(n):
    matrix.append([int(x) for x in input().split()])
    primary_diagonal_sum += matrix[row][row]

for row in range(n):
    for col in range(n):
        if row + col == n -1:
            secondary_diagonal_sum += matrix[row][col]


print(abs(primary_diagonal_sum - secondary_diagonal_sum))

