class Ship:
    def __init__(self):
        self.coordinates = []
        self.length = 3
        self.has_invalid_coords = True

    def str_list_to_coords(self, str_list):
        return [[ord(str[0]) - 97, int(str[1:])] for str in str_list]
        
    def set_coordinates(self):
        while(True):
            usr_inpt = input(f'Please enter ({self.length}) coordinates for your {self.name} (separated by commas)\n>>>').lower()
            formatted_input = [str.strip() for str in usr_inpt.split(',')]

            try:
                coordinates = self.str_list_to_coords(formatted_input)
            except ValueError:
                print('Invalid input. Please try again.')
                return True
            
            self.coordinates = coordinates
            return False

class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Destroyer'
        self.length = 2
        self.icon = '/ /'

class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Submarine'
        self.length = 3
        self.icon = '( )'

class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Battleship'
        self.length = 4
        self.icon = '{ }'

class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = 'Aircraft Carrier'
        self.length = 5
        self.icon = '[ ]'