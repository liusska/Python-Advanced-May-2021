rows, cols = [int(x) for x in input().split()]
matrix = []
equals = 0

for row in range(rows):
    matrix.append(input().split())

for row in range(rows-1):
    for col in range(len(matrix[row])-1):
        if matrix[row][col] == matrix[row][col+1]==matrix[row+1][col] == matrix[row+1][col+1]:
            equals += 1

print(equals)
