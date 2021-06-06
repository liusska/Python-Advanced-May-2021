rows_count = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows_count)]

while True:
    command = input()
    if command == "END":
        break
    tokens = command.split(" ")
    action = tokens[0]
    current_row = int(tokens[1])
    current_col = int(tokens[2])
    number = int(tokens[3])
    if current_row >= rows_count or current_col >= rows_count or current_col < 0 or current_row < 0:
        print("Invalid coordinates")
    else:
        if action == "Add":
            for row in range(len(matrix)):
                for col in range(len(matrix)):
                    if current_col == col and current_row == row:
                        matrix[row][col] += number
        elif action == "Subtract":
            for row in range(len(matrix)):
                for col in range(len(matrix)):
                    if current_col == col and current_row == row:
                        matrix[row][col] -= number

for i in range(len(matrix)):
    print(' '.join([str(x) for x in matrix[i]]))