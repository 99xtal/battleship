class Ship:
    def __init__(self):
        self.coordinates = []
        self.length = 3

    def set_coordinates(self):
        '''Set coordinates for ship from valid user input'''

        invalid_coordinates = True
        while(invalid_coordinates):
            # Take user input for coordinates in form 'b2, b3, b4'
            usr_inpt = input(f'Please enter ({self.length}) consecutive coordinates where you would like to place your {self.name} (separated by commas)\n>>>').lower()
            coord_str_list = [str.strip() for str in usr_inpt.split(',')]

            # Convert input coordinates to list of ordered pairs
            coords_list = self.str_list_to_coordinates(coord_str_list)
            
            # Check for invalid coordinates
            invalid_coordinates = self.check_invalid_coordinates(coords_list)
            if not invalid_coordinates:
                self.coordinates = coords_list
            
            
    def check_invalid_coordinates(self, coords_list):
        # Check correct number of coordinates
        if len(coords_list) != self.length:
            print('Invalid number of coordinates. Please try again.')
            return True

        # Check correct ship orientation
        matching_row_values = [coord[0] for coord in coords_list if coord[0] == coords_list[0][0]]
        matching_col_values = [coord[1] for coord in coords_list if coord[1] == coords_list[0][1]]
        if len(matching_row_values) != self.length and len(matching_col_values) != self.length:
            print('Invalid coordinates: Ships must be oriented vertically or horizontally')
            return True

        return False

    def str_list_to_coordinates(self, str_list):
        coordinates = []
        for str in str_list:
            row = ord(str[0]) - 97
            col = int(str[1:])
            coordinates.append([row,col])
        return coordinates
   
            
class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Destroyer'
        self.length = 2

class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Submarine'
        self.length = 3

class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Battleship'
        self.length = 4

class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Aircraft Carrier'
        self.length = 5