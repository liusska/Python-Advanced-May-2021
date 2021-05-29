import sys

rows, cols = [int(x) for x in input().split()]
matrix = []
result = -sys.maxsize
position = None

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for row in range(rows-2):
    for col in range(len(matrix[row])-2):
        current_result = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] + \
                matrix[row+1][col] + matrix[row+1][col+1] + matrix[row+1][col+2] + \
                matrix[row+2][col] + matrix[row+2][col+1] + matrix[row+2][col+2]
        if current_result > result:
            result = current_result
            position = f'{matrix[row][col]} {matrix[row][col + 1]} {matrix[row][col + 2]}\n' \
                       f'{matrix[row + 1][col]} {matrix[row + 1][col + 1]} {matrix[row + 1][col + 2]}\n' \
                       f'{matrix[row + 2][col]} {matrix[row + 2][col + 1]} {matrix[row + 2][col + 2]}'

print(f'Sum = {result}')
print(position)