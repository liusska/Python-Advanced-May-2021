def valid_move(rows, cols):
    if rows in range(n) and cols in range(n):
        return rows, cols
    return False


def find_player():
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'P':
                return i, j


data = list(input())
n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input()))

moves = int(input())
row, col = find_player()

for move in range(moves):
    current_move = None
    command = input()
    if command == 'up':
        current_move = valid_move(row-1, col)
    elif command == 'down':
        current_move = valid_move(row+1, col)
    elif command == 'left':
        current_move = valid_move(row, col-1)
    elif command == 'right':
        current_move = valid_move(row, col+1)

    if current_move:
        current_row, current_col = current_move
        if not matrix[current_row][current_col] == '-':
            data.append(matrix[current_row][current_col])
        matrix[row][col] = '-'
        matrix[current_row][current_col] = 'P'
        row = current_row
        col = current_col
    else:
        data.pop()

print(''.join(data))
for row in range(len(matrix)):
    print(''.join([str(x) for x in matrix[row]]))

