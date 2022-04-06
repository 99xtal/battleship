from player import *

class Game():
    def __init__(self):
        self.players = [Player('Player 1'), Player('Player 2')]

    def game_setup(self):
        '''Run player setup for each player'''
        for player in self.players:
            player.initial_setup()

    def run_game(self):
        '''Main game loop'''
        self.game_setup()


game = Game()
game.run_game()
