from player import *

class Game():
    def __init__(self):
        self.players = [Player('Player 1'), Player('Player 2')]

    def player_setup(self):
        for player in self.players:
            player.set_name()
            player.place_ships()

    def run_game(self):
        self.player_setup()


game = Game()
game.run_game()