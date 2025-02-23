import random

def roll_dice():
    return random.randint(1, 6)

snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}

def move_player(position):
    dice_value = roll_dice()
    print(f"Rolled: {dice_value}")
    position += dice_value

    if position in snakes:
        print(f"Oops! Bitten by a snake at {position}")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder at {position}")
        position = ladders[position]

    if position > 100:
        position -= dice_value  # Prevent going beyond 100

    print(f"New Position: {position}\n")
    return position

def play_game():
    print("Welcome to Snake and Ladder!")
    player_choice = int(input("Choose your position: 1 for Player 1, 2 for Player 2: "))

    player1, player2 = 0, 0

    while player1 < 100 and player2 < 100:
        if player_choice == 1:
            input("Player 1, press Enter to roll the dice...")
            player1 = move_player(player1)
            if player1 == 100:
                print("Player 1 Wins!")
                break

            input("Player 2, press Enter to roll the dice...")
            player2 = move_player(player2)
            if player2 == 100:
                print("Player 2 Wins!")
                break
        else:
            input("Player 2, press Enter to roll the dice...")
            player2 = move_player(player2)
            if player2 == 100:
                print("Player 2 Wins!")
                break

            input("Player 1, press Enter to roll the dice...")
            player1 = move_player(player1)
            if player1 == 100:
                print("Player 1 Wins!")
                break

if __name__ == "__main__":
    play_game()

