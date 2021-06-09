def check_valid_position(row, col):
    if row in range(n) and col in range(n):
        if matrix[row][col] == '*':
            return 1
    return 0


def get_position(data):
    new_data = ''
    for i in range(1, len(data)-1):
        new_data += data[i]
    return new_data.split(', ')


def calculate_cells(b_matrix):
    for i in range(len(b_matrix)):
        for j in range(len(b_matrix)):
            bombs_in_area = 0
            if matrix[i][j] == '':
                up_position= check_valid_position(i-1, j)
                bombs_in_area += up_position
                down_position = check_valid_position(i+1, j)
                bombs_in_area += down_position
                left_position = check_valid_position(i, j-1)
                bombs_in_area += left_position
                right_position = check_valid_position(i, j+1)
                bombs_in_area += right_position
                left_up_diagonal = check_valid_position(i-1, j-1)
                bombs_in_area += left_up_diagonal
                left_down_diagonal = check_valid_position(i+1, j-1)
                bombs_in_area += left_down_diagonal
                right_up_diagonal = check_valid_position(i-1, j+1)
                bombs_in_area += right_up_diagonal
                right_down_diagonal = check_valid_position(i+1, j+1)
                bombs_in_area += right_down_diagonal
                matrix[i][j] = bombs_in_area

    return matrix


n = int(input())
bombs = int(input())

matrix = []
for rows in range(n):
    row = []
    for cols in range(n):
        row.append('')
    matrix.append(row)


for _ in range(bombs):
    row, col = get_position(input())
    matrix[int(row)][int(col)] = '*'

matrix = calculate_cells(matrix)

for row in matrix:
    print(' '.join([str(x) for x in row]))
