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
        self.guess_history = []

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
    def __init__(self, default_name):
        super().__init__(default_name)

    def _place_ships(self):
        self.ships[0].set_manually([0,0],[0,1])
        self.ships[1].set_manually([1,0],[1,1],[1,2])
        self.ships[2].set_manually([2,0],[2,1],[2,2],[2,3])
        self.ships[3].set_manually([3,0],[3,1],[3,2],[3,3])
        self.ships[4].set_manually([4,0],[4,1],[4,2],[4,3],[4,4])

        for ship in self.ships:
            self.ship_grid.add_ship(ship)
