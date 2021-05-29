rows, cols = [int(x) for x in input().split()]
matrix = []

for row in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == 'END':
        break
    if len(command.split()) == 5:
        action, row_1, col_1,  row_2, col_2 = command.split()
        if action == 'swap':
            row_1 = int(row_1)
            col_1 = int(col_1)
            row_2 = int(row_2)
            col_2 = int(col_2)

            if row_1 in range(rows) and row_2 in range(rows) and \
                    col_1 in range(cols) and col_2 in range(cols):
                matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
                for row in range(len(matrix)):
                    print(f'{" ".join(matrix[row])}')
            else:
                print(f'Invalid input!')

        else:
            print(f'Invalid input!')

    else:
        print(f'Invalid input!')
