from collections import deque


def bunnie_spread_action(matrix_to_spread, row, col):
    a=5
    if matrix_to_spread[row][col] == '.':
        matrix_to_spread[row][col] = 'BB'
    elif matrix_to_spread[row][col] == 'P':
        matrix_to_spread[row][col] = 'BB'
        dead = True
    return matrix_to_spread


def valid_idx(i, j):
    a=5
    if i in range(rows) and j in range(cols):
        return i, j
    return False


def find_player(matrix_to_search):
    a=5
    for i in range(len(matrix_to_search)):
        for j in range(len(matrix_to_search[i])):
            if matrix_to_search[i][j] == 'P':
                return i, j


def bunnie_spread(matrix_to_spread):
    for i in range(len(matrix_to_spread)):
        for j in range(len(matrix_to_spread[i])):
            if matrix_to_spread[i][j] == 'B':

                if valid_idx(i-1, j):
                    row_spread, col_spread = valid_idx(i-1, j)
                    matrix_to_spread = bunnie_spread_action(matrix, row_spread, col_spread)

                if valid_idx(i+1, j):
                    row_spread, col_spread = valid_idx(i+1, j)
                    matrix_to_spread = bunnie_spread_action(matrix, row_spread, col_spread)

                if valid_idx(i, j-1):
                    row_spread, col_spread = valid_idx(i, j-1)
                    matrix_to_spread = bunnie_spread_action(matrix, row_spread, col_spread)

                if valid_idx(i, j+1):
                    row_spread, col_spread = valid_idx(i, j+1)
                    matrix_to_spread = bunnie_spread_action(matrix, row_spread, col_spread)

    for i in range(rows):
        for j in range(cols):
            if matrix_to_spread[i][j] == 'BB':
                matrix_to_spread[i][j] = 'B'
    return matrix_to_spread


rows, cols = [int(x) for x in input().split()]
matrix = []
dead = False
win = False
last_move = []


for _ in range(rows):
    matrix.append(list(input()))

actions = deque(input())
valid_move = False

while actions:
    row, col = find_player(matrix)
    action = actions.popleft()

    if action == 'U':
        valid_move = valid_idx(row-1, col)
    elif action == 'D':
        valid_move = valid_idx(row + 1, col)
    elif action == 'L':
        valid_move = valid_idx(row, col - 1)
    elif action == 'R':
        valid_move = valid_idx(row, col + 1)

    if valid_move:
        move_row, move_col = valid_move
        last_move.append([move_row, move_col])
        if matrix[move_row][move_col] == 'B':
            dead = True
            win = False
        if matrix[move_row][move_col] == '.':
            matrix[move_row][move_col] = 'P'
            matrix[row][col] = '.'
            dead = False
            win = False

        matrix = bunnie_spread(matrix)

    elif not valid_move and not dead:
        last_move.append([row, col])
        won = True
        dead = False
        for i in range(len(matrix)):
            for j in range(len(matrix[row])):
                if matrix[i][j] == 'P':
                    matrix[i][j] = '.'
                    last_move.append([i, j])
        matrix = bunnie_spread(matrix)

    if not find_player(matrix):
        dead = True
        break

    if not actions:
        win = True
        break


for row in range(len(matrix)):
    print(''.join(matrix[row]))

if last_move:
    row, col = last_move.pop()
    if win:
        print(f'won: {row} {col}')
    elif not actions:
        print(f'won: {row} {col}')
    else:
        print(f'dead: {row} {col}')



