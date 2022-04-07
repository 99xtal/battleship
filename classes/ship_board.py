from .board import Board
from .ships import *

class ShipBoard(Board):
    def __init__(self, player_name, area):
        super().__init__(player_name, area)
        self.ships = [Destroyer(), Submarine(), Battleship(), Battleship(), AircraftCarrier()]
        self.placement_conditions = [self.has_valid_num_of_coordinates,
                                    self.has_consecutive_coordinates,
                                    self.is_within_board,
                                    self.doesnt_overlap_placed_ships]
        self.place_ships()

    def get_centered_board_name(self):
        title = f'{self.player_name.title()}\'s Ships'
        return self.center_text_on_board(title)

    # SHIP PLACEMENT
    def place_ships(self):
        '''Place ships on board and check for invalid coordinates'''
        self.render()
        for ship in self.ships:
            while ship.has_invalid_coords:
                ship.set_coordinates()
                self.validate_coordinates(ship)
                if not ship.has_invalid_coords:
                    self.add_ships_to_board()
                    self.render()

    def validate_coordinates(self, ship):
        '''Check ship coordinates against each placement condition'''
        for condition in self.placement_conditions:
            if condition(ship) == False:
                print('Error: Invalid coordinates. Please try again')
                return
        ship.has_invalid_coords = False
        

    def add_ships_to_board(self):
        for ship in self.ships:
            for coord in ship.coordinates:
                self.board[coord[0]][coord[1]] = '[ ]'

    # PLACEMENT CONDITIONS
    def has_valid_num_of_coordinates(self, ship):
        if not len(ship.coordinates) == ship.length:
            print("Error: Number of coordinates must match ship size.")
            return False
        return True

    def has_consecutive_coordinates(self, ship):
        has_consecutive_rows, has_consecutive_cols = True, True

        for i in range(1,ship.length):
            if ship.coordinates[i][0] != ship.coordinates[i-1][0] + 1:
                has_consecutive_rows = False
            if ship.coordinates[i][1] != ship.coordinates[i-1][1] + 1:
                has_consecutive_cols = False
        return has_consecutive_rows or has_consecutive_cols

    def is_within_board(self, ship):
        if not all(x[0] in range(self.area) and x[1] in range(self.area) for x in ship.coordinates):
            print('Error: Coordinates out of bound of board.')


    def doesnt_overlap_placed_ships(self, ship):
        '''Check that ship doesn't overlap with any other ship already on the board'''
        placed_ships = [_ for _ in self.ships if _ != ship]
        for coord in ship.coordinates:
            for placed_ship in placed_ships:
                if coord in placed_ship.coordinates:
                    print(f'Error: {ship.name} placement overlaps {placed_ship.name}.')
                    return False
        return True