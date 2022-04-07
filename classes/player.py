from .board import Board
from .ship_board import ShipBoard
from .ships import *

class Player():
    def __init__(self, name):
        self.name = name
        self.ship_board = None
        self.guess_board = None

    def run_setup(self):
        '''Setup steps for each player'''
        self._set_name()
        self._initialize_boards()

    def _set_name(self):
        '''Allow user to set player name'''
        usr_input = input(f'{self.name.upper()}, please enter your name:\n>>> ')     
        self.name = usr_input
        print(f'Welcome {self.name.upper()}.\n')
        
    def _initialize_boards(self):
        '''Set up ship and guess boards with player name'''
        self.ship_board = ShipBoard(self.name, 20)
        self.guess_board = Board(self.name, 20)