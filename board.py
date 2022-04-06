from ships import *

class Board():
    def __init__(self, player_name, area):
        self.player_name = player_name
        self.area = area
        self.board = [['   ' for i in range(self.area)] for i in range(self.area)]
 
    #  RENDERING THE BOARD

    def row_values_to_string(self, row_values):
        str = ''
        for point in row_values:
            str += f'{point}|'
        return str

    def get_board_name(self):
        return f'{self.player_name.title()}\'s Guesses'

    def get_column_numbers(self):
        col_num_string = ' '
        for i in range(self.area):
            if i < 10:
                col_num_string += f'   {i}'
            else:
                col_num_string += f'  {i}'
        return col_num_string

    def render(self):
        print(self.get_board_name())
        print(self.get_column_numbers())
        for i, row in enumerate(self.board):
            print(f'{chr(i + 65)} |{self.row_values_to_string(row)}')


class ShipBoard(Board):
    def __init__(self, player_name, area):
        super().__init__(player_name, area)
        self.ships = [Destroyer(), Submarine(), Battleship(), Battleship(), AircraftCarrier()]

    def get_board_name(self):
        return f'\t\t{self.player_name.title()}\'s Ships'

    def place_ships(self):
        for ship in self.ships:
            self.render()
            while ship.has_invalid_coords:
                ship.set_coordinates()
                self.validate_ship_coordinates(ship)
                if not ship.has_invalid_coords:
                    self.add_ships_to_board()

    def validate_ship_coordinates(self, ship):
        
        within_board = all(coord[0] in range(self.area) and coord[1] in range(self.area) for coord in ship.coordinates)

        if not ship.has_valid_number_of_coordinates():
            print('Invalid number of coordinates. Please try again')
        elif not ship.has_valid_orientation():
            print('Invalid coordinates: Ships must be oriented vertically or horizontally. Please try again.')
        elif not ship.has_consecutive_coordinates():
            print('Invalid coordinates: Coordinates must be consecutive')
        elif not within_board:
            print('Invalid coordinates: Ship must be placed within area of the board')
        elif self.overlaps_other_ships(ship):
            print(f'Invalid coordinates: {ship.name} cannot overlap any other ship.')
        else:
            ship.has_invalid_coords = False

    def overlaps_other_ships(self, ship):
        other_ships = [x for x in self.ships if x != ship]

        for coord in ship.coordinates:
            for other_ship in other_ships:
                if coord in other_ship.coordinates:
                    return True
        return False

    def add_ships_to_board(self):
        for ship in self.ships:
            for coord in ship.coordinates:
                self.board[coord[0]][coord[1]] = '[ ]'