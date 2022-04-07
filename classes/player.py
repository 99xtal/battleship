from .board import Board
from .ship_board import ShipBoard
from .ships import Destroyer, Submarine, Battleship, AircraftCarrier

class Player():
    def __init__(self, name):
        self.name = name
        self.ship_board = None
        self.guess_board = None
        self.ships = [Destroyer(), Submarine(), Battleship(), Battleship(), AircraftCarrier()]
        self.placement_conditions = [self.has_valid_num_of_coordinates,
                                    self.has_consecutive_coordinates,
                                    self.is_within_board,
                                    self.doesnt_overlap_other_ships]

    def run_setup(self):
        self.set_name()
        self.initialize_boards()
        self.intialize_ships()

    def set_name(self):
        usr_input = input(f'{self.name.upper()}, please enter your name:\n>>> ')     
        self.name = usr_input
        print(f'Welcome {self.name.upper()}.\n')
        
    def initialize_boards(self):
        self.ship_board = ShipBoard(self.name, 20)
        self.guess_board = Board(self.name, 20)

    def intialize_ships(self):
        self.ship_board.render()
        for ship in self.ships:
            while ship.has_invalid_coords:
                ship.set_coordinates()
                self.validate_coordinates(ship)
                if not ship.has_invalid_coords:
                    self.ship_board.add_ship(ship)
                    self.ship_board.render()

    def validate_coordinates(self, ship):
        for condition in self.placement_conditions:
            if not condition(ship):
                return
        ship.has_invalid_coords = False
    

    # SHIP PLACEMENT CONDITIONS

    def has_valid_num_of_coordinates(self, ship):
        if not len(ship.coordinates) == ship.length:
            print('Error: Number of coordinates must match ship size.')
            return False
        return True

    def has_consecutive_coordinates(self, ship):
        has_consecutive_rows = all(ship.coordinates[i][0] == ship.coordinates[i-1][0] + 1
                                    for i in range(1, ship.length))
        has_consecutive_cols = all(ship.coordinates[i][1] == ship.coordinates[i-1][1] + 1
                                    for i in range(1, ship.length))
        
        if not (has_consecutive_rows or has_consecutive_cols):
            print('Error: Ship coordinates must be next to each other.')
            return False
        return True

    def is_within_board(self, ship):
        if not all(coord[0] in range(self.ship_board.area) and
                coord[1] in range(self.ship_board.area) for coord in ship.coordinates):
                print('Error: Ship coordinates must be within space of board.')
                return False
        return True

    def doesnt_overlap_other_ships(self, ship):
        other_ships = [x for x in self.ships if x != ship]
        for other_ship in other_ships:
            for coord in ship.coordinates:
                if coord in other_ship.coordinates:
                    print(f'Error: {ship.name} placement overlaps {other_ship.name}.')
                    return False
        return True
