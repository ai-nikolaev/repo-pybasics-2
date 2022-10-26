import random


TOTAL_SWEETS = 220
MAX_SWEETS_PER_STEP = 28

player1_total_sweets = 0
player2_total_sweets = 0

player1_is_ready = False
player2_is_ready = False
while True:
    player1 = random.randint(1, 100)
    player2 = random.randint(1, 100)
    if player1 > player2:
        player1_is_ready = True
        break
    elif player2 > player1:
        player2_is_ready = True
        break

print(player1_is_ready)
print(player2_is_ready)

while True:
    if player1_is_ready:
        player_sweets = int(
            input(f"Игрок 1: Введите количество конфет (не более {MAX_SWEETS_PER_STEP}): "))
        if player_sweets > MAX_SWEETS_PER_STEP:
            continue
        if TOTAL_SWEETS >= player_sweets:
            player1_total_sweets += player_sweets
            TOTAL_SWEETS -= player_sweets
        else:
            player1_total_sweets += TOTAL_SWEETS
            TOTAL_SWEETS = 0
        player1_is_ready = False
        player2_is_ready = True
    elif player2_is_ready:
        player_sweets = int(
            input(f"Игрок 2: Введите количество конфет (не более {MAX_SWEETS_PER_STEP}): "))
        if player_sweets > MAX_SWEETS_PER_STEP:
            continue
        if TOTAL_SWEETS >= player_sweets:
            player2_total_sweets += player_sweets
            TOTAL_SWEETS -= player_sweets
        else:
            player2_total_sweets += TOTAL_SWEETS
            TOTAL_SWEETS = 0
        player1_is_ready = True
        player2_is_ready = False
    print(f'Конфет на столе: {TOTAL_SWEETS}')
    if TOTAL_SWEETS <= 0:
        if player1_is_ready:
            player2_total_sweets += player1_total_sweets
            print(f'Победил Игрок 2! Конфет: {player2_total_sweets}')
            break
        elif player2_is_ready:
            player1_total_sweets += player2_total_sweets
            print(f'Победил Игрок 1! Конфет: {player1_total_sweets}')
            break
