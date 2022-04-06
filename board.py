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

    def center_text_on_board(self, text):
        board_length = 4*self.area + 3
        center_point = board_length/2
        indent = int(center_point - len(text)/2)
        return ' ' * indent + text

    def get_centered_board_name(self):
        title = f'{self.player_name.title()}\'s Guesses'
        return self.center_text_on_board(title)

    def get_column_numbers(self):
        col_num_string = ' '
        for i in range(self.area):
            if i < 10:
                col_num_string += f'   {i}'
            else:
                col_num_string += f'  {i}'
        return col_num_string

    def render(self):
        print(self.get_centered_board_name())
        print(self.get_column_numbers())
        for i, row in enumerate(self.board):
            print(f'{chr(i + 65)} |{self.row_values_to_string(row)}')


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

    def place_ships(self):
        '''Place ships on board and check for invalid coordinates'''
        for ship in self.ships:
            self.render()
            while ship.has_invalid_coords:
                ship.set_coordinates()
                ship.has_invalid_coords = self.are_coordinates_invalid(ship)
                if not ship.has_invalid_coords:
                    self.add_ships_to_board()

    def are_coordinates_invalid(self, ship):
        '''Check ship coordinates against each placement condition'''
        for condition in self.placement_conditions:
            if condition(ship) == False:
                print('Error: Invalid coordinates. Please try again')
                return True
        return False

    def add_ships_to_board(self):
        for ship in self.ships:
            for coord in ship.coordinates:
                self.board[coord[0]][coord[1]] = '[ ]'

    # PLACEMENT RULES
    def has_valid_num_of_coordinates(self, ship):
        '''Check that ship has valid number of coordinates'''
        if len(ship.coordinates) != ship.length:
            return False
        return True

    def has_consecutive_coordinates(self, ship):
        '''Check that ship coordinates are consecutive'''
        has_consecutive_rows, has_consecutive_cols = True, True
        for i in range(1,ship.length):
            if ship.coordinates[i][0] != ship.coordinates[i-1][0] + 1:
                has_consecutive_rows = False
            if ship.coordinates[i][1] != ship.coordinates[i-1][1] + 1:
                has_consecutive_cols = False
        return has_consecutive_rows or has_consecutive_cols

    def doesnt_overlap_placed_ships(self, ship):
        '''Check that ship doesn't overlap with any other ship already on the board'''
        placed_ships = [x for x in self.ships if x != ship]

        for coord in ship.coordinates:
            for placed_ship in placed_ships:
                if coord in placed_ship.coordinates:
                    return False
        return True

    def is_within_board(self, ship):
        '''Check that ship placement is within board area'''
        for coord in ship.coordinates:
            if coord[0] not in range(self.area) or coord[1] not in range(self.area):
                return False
        return True

