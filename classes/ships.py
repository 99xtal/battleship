from .prompt import CoordinatePrompt

class Ship:
    def __init__(self):
        self.name = 'Generic Ship'
        self.coordinates = []
        self.length = 3
        self.is_valid = False

    def __repr__(self):
        return f'Ship({self.name}, {self.coordinates})'

    def __len__(self):
        return self.length

    def set_coordinates(self):
        self.coordinates = CoordinatePrompt(self).get_output()

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