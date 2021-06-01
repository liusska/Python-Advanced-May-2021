import math


def valid_idx(row, col):
    if row in range(n) and col in range(n):
        return (row, col)
    return False


def find_player():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'P':
                return (i, j)


n = int(input())
coins = 0
matrix_moves = []
dead = False

matrix = []
for _ in range(n):
    matrix.append(input().split())

row, col = find_player()
while coins < 100:
    action = input()

    if action == 'up':
        valid_move = valid_idx(row-1, col)
    elif action == 'down':
        valid_move = valid_idx(row + 1, col)
    elif action == 'left':
        valid_move = valid_idx(row, col - 1)
    elif action == 'right':
        valid_move = valid_idx(row, col + 1)
    else:
        continue
    if valid_move:
        move_row, move_col = valid_move
        if matrix[move_row][move_col] == 'X':
            coins = math.floor(coins / 2)
            dead = True
            break
        else:
            coins += int(matrix[move_row][move_col])
            row = move_row
            col = move_col

    else:
        coins = math.floor(coins / 2)
        dead = True
        break
    matrix_moves.append([move_row, move_col])

if not dead:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print(f'Your path:')
for row in matrix_moves:
    print(row)
