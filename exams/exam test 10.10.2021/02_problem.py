def shoot_target(matrix, direction, row, col):
    if direction == 'right':
        for i in range(5):
            for j in range(5):
                if i == row and j >= col:
                    if matrix[i][j] == 'x':
                        matrix[i][j] = '.'
                        steps_position.append([i, j])
                        return matrix
    elif direction == 'left':
        for i in range(5):
            for j in reversed(range(5)):
                if i == row and j <= col:
                    if matrix[i][j] == 'x':
                        matrix[i][j] = '.'
                        steps_position.append([i, j])
                        return matrix
    elif direction == 'up':
        for i in reversed(range(5)):
            for j in range(5):
                if i <= row and j == col:
                    if matrix[i][j] == 'x':
                        matrix[i][j] = '.'
                        steps_position.append([i, j])
                        return matrix
    elif direction == 'down':
        for i in range(5):
            for j in range(5):
                if i >= row and j == col:
                    if matrix[i][j] == 'x':
                        matrix[i][j] = '.'
                        steps_position.append([i, j])
                        return matrix
    return matrix


def valid_position(rows, cols):
    if rows in range(5) and cols in range(5):
        return rows, cols
    return False


def find_player():
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 'A':
                return i, j


def check_for_targets():
    target_count = 0
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 'x':
                target_count += 1
    if target_count > 0:
        return target_count
    return 0


matrix = []
for _ in range(5):
    matrix.append(input().split(' '))

all_targets = check_for_targets()
steps_position = []


n = int(input())
for _ in range(n):
    row, col = find_player()
    position = False
    command = input().split()
    if command[0] == 'move':
        steps = int(command[2])
        if command[1] == 'right':
            position = valid_position(row, col+steps)
        elif command[1] == 'left':
            position = valid_position(row, col-steps)
        elif command[1] == 'up':
            position = valid_position(row-steps, col)
        elif command[1] == 'down':
            position = valid_position(row+steps, col)

        if position:
            row_steps, col_steps = position
            if matrix[row_steps][col_steps] == '.':
                matrix[row][col] = '.'
                matrix[row_steps][col_steps] = 'A'

    elif command[0] == 'shoot':
        if check_for_targets() > 0:
            matrix = shoot_target(matrix, command[1], row, col)
        else:
            break

    targets_left = check_for_targets()
    if targets_left == 0:
        break


targets_left = check_for_targets()
if targets_left > 0:
    print(f"Training not completed! {targets_left} targets left.")
else:
    print(f"Training completed! All {all_targets} targets hit.")

for row in steps_position:
    print(row)