from .player import Player

class Game():
    def __init__(self):
        self.players = [Player('Player 1'), Player('Player 2')]

    def _run_player_setup(self):
        '''Run player setup for each player'''
        for player in self.players:
            player.run_setup()

    def run_game(self):
        '''Main game loop'''
        self._run_player_setup()


game = Game()
game.run_game()
