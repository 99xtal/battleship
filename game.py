from player import *

class Game():
    def __init__(self):
        self.players = [Player('Player 1'), Player('Player 2')]

    def game_setup(self):
        for player in self.players:
            player.initial_setup()

    def run_game(self):
        self.game_setup()


game = Game()
game.run_game()