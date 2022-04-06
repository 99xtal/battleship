from board import Board
from ships import *

class Player():
    def __init__(self, name):
        self.name = name
        self.ship_board = Board(20)
        self.guess_board = Board(20)
        self.ships = [Destroyer(), Submarine(), Battleship(), Battleship(), AircraftCarrier()]


    def set_name(self):
        usr_input = input(f'{self.name.upper()}, please enter your name:\n>>> ')     
        self.name = usr_input
        print(f'Welcome {self.name.upper()}.\n')

    def place_ships(self):
        for ship in self.ships:
            ship.set_coordinates()