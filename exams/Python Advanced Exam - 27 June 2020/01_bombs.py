from collections import deque

effects = deque(int(x) for x in input().split(', '))
casings = [int(x) for x in input().split(', ')]

DATURA = 40
CHERRY = 60
SMOKE_DECOY = 120

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0
fill_bomb_pouch = False


while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()
    current_sum = effect + casing
    if current_sum == DATURA:
        datura_bombs += 1
    elif current_sum == CHERRY:
        cherry_bombs += 1
    elif current_sum == SMOKE_DECOY:
        smoke_decoy_bombs += 1
    else:
        effects.appendleft(effect)
        casings.append(casing - 5)
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        fill_bomb_pouch = True
        break


if fill_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in effects])}")
else:
    print("Bomb Effects: empty")

if casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in casings])}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")
