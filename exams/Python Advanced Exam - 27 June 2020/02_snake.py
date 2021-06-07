def check_valid_position(rows, cols):
    if rows in range(n) and cols in range(n):
        return rows, cols
    return False


def find_position_of(sign):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == sign:
                return i, j


n = int(input())

food_quantity = 0
win = True

matrix = []
for _ in range(n):
    matrix.append(list(input()))

s_row, s_col = find_position_of('S')

while food_quantity < 10:
    valid_position = False
    command = input()
    if command == "up":
        valid_position = check_valid_position(s_row-1, s_col)
    elif command == 'down':
        valid_position = check_valid_position(s_row+1, s_col)
    elif command == 'left':
        valid_position = check_valid_position(s_row, s_col-1)
    elif command == 'right':
        valid_position = check_valid_position(s_row, s_col+1)

    if valid_position:
        row, col = valid_position

        if matrix[row][col] == '-':
            matrix[s_row][s_col] = '.'
            matrix[row][col] = 'S'

        elif matrix[row][col] == '*':
            food_quantity += 1
            if food_quantity <= 10:
                matrix[s_row][s_col] = '.'
                matrix[row][col] = 'S'

        elif matrix[row][col] == 'B':
            matrix[s_row][s_col] = '.'
            matrix[row][col] = '.'
            b_rows, b_cols = find_position_of('B')
            matrix[b_rows][b_cols] = 'S'
            row = b_rows
            col = b_cols
            win = False

        s_row = row
        s_col = col
    else:
        last_row, last_col = find_position_of('S')
        matrix[last_row][last_col] = '.'
        win = False
        break

if win or food_quantity >= 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food_quantity}")

for row in matrix:
    print(''.join(row))
