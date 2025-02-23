import random

class SnakeAndLadder:
    def __init__(self, num_players):
        self.board_size = 100
        self.snakes = {99: 7, 65: 52, 25: 5, 88: 24}
        self.ladders = {3: 22, 6: 25, 11: 40, 60: 85, 45: 90}
        self.players = {f"Player {i+1}": 0 for i in range(num_players)}

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player):
        roll = self.roll_dice()
        new_position = self.players[player] + roll
        if new_position > self.board_size:
            print(f"{player} rolled {roll}, but needs an exact roll to reach 100.")
            return
        
        if new_position in self.snakes:
            print(f"{player} rolled {roll} and got bitten by a snake! Down to {self.snakes[new_position]}")
            new_position = self.snakes[new_position]
        elif new_position in self.ladders:
            print(f"{player} rolled {roll} and climbed a ladder! Up to {self.ladders[new_position]}")
            new_position = self.ladders[new_position]
        else:
            print(f"{player} rolled {roll} and moved to {new_position}")
        
        self.players[player] = new_position

    def play_game(self):
        print("\n--- Starting Snake and Ladder Game ---")
        while True:
            for player in self.players.keys():
                input(f"{player}'s turn. Press Enter to roll the dice...")
                self.move_player(player)
                if self.players[player] == self.board_size:
                    print(f"\n🎉 {player} wins the game! 🎉")
                    return  # End the game

if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    game = SnakeAndLadder(num_players)
    game.play_game()