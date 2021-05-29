from collections import deque

rows, cols = [int(x) for x in input().split()]

word = deque(input())
matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append('')

for row in range(rows):
    for col in range(cols):
        current_col = col
        current_ch = word.popleft()
        if not row % 2 == 0:
            current_col = cols - 1 - col
        matrix[row][current_col] = current_ch
        word.append(current_ch)

for row in matrix:
    print(''.join(row))