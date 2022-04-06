class Ship:
    def __init__(self):
        self.coordinates = []
        self.length = 3
        self.has_invalid_coords = True

    def set_coordinates(self):
        '''Set coordinates for ship from valid user input'''

        bad_input = True
        while(True):
            # Take user input for coordinates in form 'b2, b3, b4'
            usr_inpt = input(f'Please enter ({self.length}) consecutive coordinates where you would like to place your {self.name} (separated by commas)\n>>>').lower()
            coord_str_list = [str.strip() for str in usr_inpt.split(',')]

            try:
                coords_list = self.str_list_to_coordinates(coord_str_list)
            except ValueError:
                print('Invalid input. Please try again.')
                return True
            
            self.coordinates = coords_list
            return False
        
    def str_list_to_coordinates(self, str_list):
        coordinates = []
        for str in str_list:
            row = ord(str[0]) - 97
            col = int(str[1:])
            coordinates.append([row,col])
        return coordinates
   
    def has_valid_number_of_coordinates(self):
       return len(self.coordinates) == self.length

    def has_valid_orientation(self):
        has_matching_rows = all(coord[0] == self.coordinates[0][0] for coord in self.coordinates)
        has_matching_cols = all(coord[1] == self.coordinates[0][1] for coord in self.coordinates)
        if has_matching_rows and has_matching_cols:
            return False
        return True
            
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