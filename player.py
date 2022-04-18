from ships import Destroyer, Submarine, Battleship, AircraftCarrier
from grid import Grid
from prompts import CoordinatePrompt
from validators import ShipPlacementValidator


class Player:
    def __init__(self, default_name):
        self.name = self._set_name(default_name)
        self.ships = [
            Destroyer(),
            Submarine(),
            Battleship(),
            Battleship(),
            AircraftCarrier(),
        ]
        self.ship_grid = Grid(f"{self.name}'s Ships", 20, 20)
        self.guess_grid = Grid(f"{self.name}'s Guesses", 20, 20)

        self._place_ships()

    def __repr__(self):
        return f"Player({self.name})"

    def _set_name(self, default):
        """Replace default player name with custom name via user input"""
        usr_input = input(f"{default.upper()}, please enter your name:\n>>> ").title()
        print(f"Welcome {usr_input.upper()}.\n")
        return usr_input

    def _place_ships(self):
        """Prompt user to select coordinates for each ship until they dont break placement rules"""
        validator = ShipPlacementValidator()
        print(self.ship_grid)
        for ship in self.ships:
            other_ships = [_ for _ in self.ships if _ != ship]
            is_valid = False
            while not is_valid:
                ship.set_coordinates()
                is_valid = validator.validate(ship, other_ships, self.ship_grid)
            self.ship_grid.add_ship(ship)

    def choose_target(self):
        """Choose a coordinate on opponent's ship grid to send an attack"""
        print(self.guess_grid)
        prompt = CoordinatePrompt(
            f"{self.name.upper()}: Please enter a coordinate for your attack."
        )
        prompt.prompt()
        return prompt.output

    # def receive_attack(self):
    #     pass

    # def record_attack(self):
    #     pass

