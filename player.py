from board import Board, ShipBoard
from ships import *

class Player():
    def __init__(self, name):
        self.name = name
        self.ship_board = None
        self.guess_board = None


    def initialize(self):
        self.set_name()
        self.initialize_boards()
        self.ship_board.place_ships()

    def set_name(self):
        usr_input = input(f'{self.name.upper()}, please enter your name:\n>>> ')     
        self.name = usr_input
        print(f'Welcome {self.name.upper()}.\n')
        
    def initialize_boards(self):
        self.ship_board = ShipBoard(self.name, 20)
        self.guess_board = Board(self.name, 20)

    def doesnt_overlap(self, ship):
        other_ships = [x for x in self.ships if x != ship]

        for coord in ship.coordinates:
            for other_ship in other_ships:
                if coord in other_ship.coordinates:
                    return False
        return True


