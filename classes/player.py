from .ships import Destroyer, Submarine, Battleship, AircraftCarrier
from .grid import Grid
from .validators import ShipPlacementValidator


class Player():
    def __init__(self, name):
        self.name = name
        self.ships = [Destroyer(), Submarine(), Battleship(), Battleship(), AircraftCarrier()]
        self.ship_grid = None
        self.guess_grid = None

        self.set_name()
        self.create_boards()
        self.place_ships()

    def __repr__(self):
        return f'Player({self.name})'

    def set_name(self):
        usr_input = input(f'{self.name.upper()}, please enter your name:\n>>> ').title()   
        self.name = usr_input
        print(f'Welcome {self.name.upper()}.\n')
        
    def create_boards(self):
        self.ship_grid = Grid(f'{self.name.title()}\'s Ships', 20, 20)
        self.guess_grid = Grid(f'{self.name.title()}\'s Guesses', 20, 20)

    def place_ships(self):
        for ship in self.ships:
            other_ships = [_ for _ in self.ships if _ != ship]
            is_valid = False
            while(not is_valid):
                ship.set_coordinates()
                validator = ShipPlacementValidator(ship, other_ships, self.ship_grid)
                is_valid = validator.validate()
            self.ship_grid.add_ship(ship)


    # def choose_target(self):
    #     pass

    # def receive_attack(self):
    #     pass

    # def record_attack(self):
    #     pass

