from prompts import CoordinateSetPrompt


class Ship:
    def __init__(self):
        self.name = "Generic Ship"
        self.coordinates = None
        self.length = 3
        self.hits = 0
        self.sunk = False
        self.is_valid = False

    def __repr__(self):
        return f"Ship(Name:{self.name}, Coordinates:{self.coordinates})"

    def __len__(self):
        return self.length

    def set_coordinates(self):
        prompt = CoordinateSetPrompt(
            f"Please enter ({len(self)}) coordinates for your {self.name} (separated by commas)\n>>>"
        )
        prompt.prompt()
        self.coordinates = prompt.output

    def set_manually(self, *args):
        self.coordinates = [*args]


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.name = "Destroyer"
        self.length = 2
        self.icon = "/ /"


class Submarine(Ship):
    def __init__(self):
        super().__init__()
        self.name = "Submarine"
        self.length = 3
        self.icon = "( )"


class Battleship(Ship):
    def __init__(self):
        super().__init__()
        self.name = "Battleship"
        self.length = 4
        self.icon = "{ }"


class AircraftCarrier(Ship):
    def __init__(self):
        super().__init__()
        self.name = "Aircraft Carrier"
        self.length = 5
        self.icon = "[ ]"
