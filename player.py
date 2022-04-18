"""Contains all Player objects"""


from display_tools import clear_screen
from ships import Destroyer, Submarine, Battleship, AircraftCarrier
from grid import Grid
from prompts import CoordinatePrompt
from validators import ShipPlacementValidator


class Player:
    """
    Base class for representing a player

    Attributes
    ----------
    name : str
        the name of the player
    ships : Ship[]
        list of ships in the player's fleet
    ship_grid : Grid
        grid for placing ships and marking opponent attacks
    guess_grid : Grid
        grid for recording attacks against opponent
    guess_history : list
        list of coordinates of previous attacks

    Methods
    -------
    set_name():
        sets name attribute from unvalidated input
    place_ships():
        sets and validates ship placement coordinates
    choose_target():
        chooses an attack coordinate from validated input
    receive_attack():
        evaluate attack from opponent and mark ship grid
    record_attack():
        evaluate attack result and mark guess grid

    """

    def __init__(self, default_name):
        """
        Constructs necessary attributes for Player object

        Parameters
        ----------
        default_name : str
            default display name for player before name input
        """
        self.name = default_name
        self.ships = [
            Destroyer(),
            Submarine(),
            Battleship(),
            Battleship(),
            AircraftCarrier(),
        ]
        self.ship_grid = Grid(20, 20)
        self.guess_grid = Grid(20, 20)
        self.guess_history = []

    def __repr__(self):
        return f"Player(Name:{self.name})"

    def set_name(self):
        """Replace default player name with custom name via user input"""
        self.name = input(f"{self.name}, please enter your name:\n>>> ").title()
        self.ship_grid.board_name = f"{self.name}'s Ships"
        self.guess_grid.board_name = f"{self.name}'s Guesses"
        print(f"Welcome {self.name}.\n")

    def place_ships(self):
        """Keep prompting user to select coordinates for each ship until they dont break placement rules"""
        validator = ShipPlacementValidator()
        for ship in self.ships:
            print(self.ship_grid)
            other_ships = [_ for _ in self.ships if _ != ship]
            is_valid = False
            while not is_valid:
                ship.set_coordinates()
                is_valid = validator.validate(ship, other_ships, self.ship_grid)
            self.ship_grid.add_ship(ship)
            clear_screen()

    def choose_target(self):
        """Choose a target coordinate for outgoing attack"""
        print(self.ship_grid)
        print(self.guess_grid)

        prompt = CoordinatePrompt(
            f"{self.name.upper()}: Please enter a coordinate for your attack."
        )
        while True:
            attack_coordinate = prompt.prompt()
            if attack_coordinate not in self.guess_history:
                self.guess_history.append(attack_coordinate)
                break
            else:
                print("You have already attacked there.")
        return attack_coordinate

    def receive_attack(self, coordinate):
        """Evaluate incoming attack as hit or miss on ship board"""
        for ship in self.ships:
            if coordinate in ship.coordinates:
                ship.hits += 1
                if ship.hits == len(ship):
                    ship.sunk = True
                self.ship_grid.mark(coordinate, "hit")
                print("Hit!")
                return "hit"
        self.ship_grid.mark(coordinate, "miss")
        print("Miss!")
        return "miss"

    def record_attack(self, target, attack_result):
        """Evaluate outgoing attack as hit or miss on guess board"""
        self.guess_grid.mark(target, attack_result)


class TestPlayer(Player):
    """
    Player with pre-set ships for testing purposes

    Overrides place_ships method
    """

    def _place_ships(self):
        self.ships[0].set_manually([0, 0], [0, 1])
        self.ships[1].set_manually([1, 0], [1, 1], [1, 2])
        self.ships[2].set_manually([2, 0], [2, 1], [2, 2], [2, 3])
        self.ships[3].set_manually([3, 0], [3, 1], [3, 2], [3, 3])
        self.ships[4].set_manually([4, 0], [4, 1], [4, 2], [4, 3], [4, 4])

        for ship in self.ships:
            self.ship_grid.add_ship(ship)
