from collections import deque


def coals_left():
    coals_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'c':
                coals_count += 1
    return coals_count


def find_miner_coordinates(matrix):
    position = None
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 's':
                position = (i, j)
    return position


def valid_index(row, col):
    if row in range(len(matrix)) and col in range(len(matrix)):
        return (row, col)
    return False


n = int(input())
directions = deque(x for x in input().split())

matrix = []
for row in range(n):
    matrix.append(input().split())

coals = 0
end_game = False
end_check = False

while directions:
    is_valid = False
    action = directions.popleft()
    miner_row, miner_col = find_miner_coordinates(matrix)
    if action == 'up':
        is_valid = valid_index(miner_row-1, miner_col)
    elif action == 'down':
        is_valid = valid_index(miner_row+1, miner_col)
    elif action == 'right':
        is_valid = valid_index(miner_row, miner_col+1)
    elif action == 'left':
        is_valid = valid_index(miner_row, miner_col-1)
    if is_valid:
        char_row, char_col = is_valid
        if matrix[char_row][char_col] == '*':
            matrix[char_row][char_col] = 's'
            matrix[miner_row][miner_col] = '*'
        elif matrix[char_row][char_col] == 'e':
            print(f'Game over! ({char_row}, {char_col})')
            end_game = True
            exit()
        elif matrix[char_row][char_col] == 'c':
            coals += 1
            matrix[char_row][char_col] = 's'
            matrix[miner_row][miner_col] = '*'
            current_coals = coals_left()
            if current_coals == 0:
                print(f"You collected all coals! ({char_row}, {char_col})")
                end_game = True
                break

    if not directions and end_game:
        print(f"Game over! ({miner_row}, {miner_col})")


if coals_left() and not end_check:
    miner_row, miner_col = find_miner_coordinates(matrix)
    print(f"{coals_left()} coals left. ({miner_row}, {miner_col})")
