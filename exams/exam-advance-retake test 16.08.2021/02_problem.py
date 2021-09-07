def make_move(row, col):
    if row in range(n) and col in range(n):
        return row, col
    return False


def find_player():
    a=5
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "A":
                matrix[i][j] = "*"
                return i, j


n = int(input())
tea_bags = 0

matrix = []
for _ in range(n):
    matrix.append(input().split())

alice_position = find_player()
command = input()

while True:
    a_row = alice_position[0]
    a_col = alice_position[1]
    alice_move = False
    if command == "down":
        alice_move = make_move(a_row+1, a_col)
    elif command == "up":
        alice_move = make_move(a_row-1, a_col)
    elif command == "left":
        alice_move = make_move(a_row, a_col-1)
    elif command == "right":
        alice_move = make_move(a_row, a_col+1)
    if not alice_move:
        break
    row, col = alice_move
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    elif matrix[row][col] == ".":
        matrix[row][col] = "*"
    elif matrix[row][col].isdigit():
        tea_bags += int(matrix[row][col])
        matrix[row][col] = "*"
    if tea_bags >= 10:
        break
    alice_position = (row, col)
    command = input()


if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

for row in range(len(matrix)):
    print(' '.join([str(x) for x in matrix[row]]))
