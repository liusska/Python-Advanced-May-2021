from math import ceil

names = input().split(', ')

player_1 = names[0]
player_2 = names[1]
players = {player_1: 501, player_2: 501}

matrix = []
for _ in range(7):
    row = [x for x in input().split()]
    matrix.append(row)

winner = False
row = 0
col = 0
player_1_count_games = 0
player_2_count_games = 0
games = 0

while players[player_1] > 0 and players[player_2] > 0:
    current_points = 0
    command = input().split(", ")
    row = int((command[0])[-1])
    col = int((command[1])[0])

    if row in range(7) and col in range(7):
        coordinate = matrix[row][col]
        if coordinate == 'D':
            current_points = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 2
        elif coordinate == 'T':
            current_points = (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 3
        elif coordinate == 'B':
            winner = True
        else:
            current_points = int(coordinate)

        if games % 2 == 0:
            player_1_count_games += 1
            if winner:
                print(f"{player_1} won the game with {player_1_count_games} throws!")
                break
            players[player_1] -= current_points
            if players[player_1] <= 0:
                print(f"{player_1} won the game with {player_1_count_games} throws!")
        else:
            player_2_count_games += 1
            if winner:
                print(f"{player_2} won the game with {player_2_count_games} throws!")
                break
            players[player_2] -= current_points
            if players[player_2] <= 0:
                print(f"{player_2} won the game with {player_2_count_games} throws!")
    else:
        if games % 2 == 0:
            player_1_count_games += 1
        else:
            player_2_count_games += 1
    games += 1

