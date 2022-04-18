"""Contains all Ship objects"""

from prompts import CoordinateSetPrompt


class Ship:
    """Base class for representing a ship

    Attributes
    ----------
    name : str
        the name of the ship
    coordinates: list
        list of ship coordinates (coordinates represented as ordered pair [x,y])
    size : int
        represents how many coordinates ship can occupy
    hits : int
        counter variable representing how many ship coordinates opponent
        has hit
    sunk : bool
        represents whether all ship coordinates have been attacked by
        opponent

    Methods
    -------

    """

    def __init__(self):
        self.name = "Generic Ship"
        self.coordinates = []
        self.size = 3
        self.hits = 0
        self.sunk = False

    def __repr__(self):
        return f"Ship(Name:{self.name}, Coordinates:{self.coordinates})"

    def __len__(self):
        return self.size

    def set_coordinates(self):
        """Set self.coordinates attribute from validated user input"""
        prompt = CoordinateSetPrompt(
            f"Please enter ({len(self)}) coordinates for your {self.name} (separated by commas)"
        )
        prompt.prompt()
        self.coordinates = prompt.output

    def set_manually(self, *args):
        """Set self.coordinates attribute from arguments

        args : all ship coordinates
        """
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
