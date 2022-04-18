class Validator:
    def __init__(self):
        self.conditions = None


class CoordinateValidator(Validator):
    def __init__(self):
        super().__init__()
        self.coordinate = None
        self.conditions = [
            self.first_character_is_alphabetic,
            self.other_characters_are_numeric,
        ]

    def first_character_is_alphabetic(self):
        if not self.coordinate[0].isalpha():
            print("Error: First character of coordinate must be a letter.")
            return False
        return True

    def other_characters_are_numeric(self):
        if not self.coordinate[1:].isnumeric():
            print("Error: Second character of coordinate must be a number.")
            return False
        return True

    def validate(self, coordinate):
        self.coordinate = coordinate
        return all(condition() for condition in self.conditions)


class ShipPlacementValidator(Validator):
    def __init__(self):
        super().__init__()
        self.ship = None
        self.other_ships = None
        self.grid = None
        self.conditions = [
            self.has_valid_num_of_coordinates,
            self.is_within_board,
            self.has_consecutive_coordinates,
            self.doesnt_overlap_other_ships,
        ]

    def validate(self, ship, other_ships, grid):
        self.ship = ship
        self.other_ships = other_ships
        self.grid = grid

        return all(condition() for condition in self.conditions)

    def has_valid_num_of_coordinates(self):
        if not len(self.ship.coordinates) == len(self.ship):
            print("Error: Number of coordinates must match ship size.")
            return False
        return True

    def is_within_board(self):
        """Check that row coordinate is within grid height, and column is within grid width"""
        width = self.grid.width
        height = self.grid.height
        coordinates = self.ship.coordinates

        if not all(
            coord[0] in range(height) and coord[1] in range(width)
            for coord in coordinates
        ):
            print("Error: Ship coordinates must be within space of board.")
            return False
        return True

    def check_consecutive_coords(self, coordinates, axis):
        """Check that all coordinates on a specified axis are consecutive"""
        for i in range(1, len(coordinates)):
            if coordinates[i][axis] != coordinates[i - 1][axis] + 1:
                return False
        return True

    def has_consecutive_coordinates(self):
        """Check that coordinates are aligned on row or column"""
        coordinates = sorted(self.ship.coordinates)

        has_consecutive_rows = self.check_consecutive_coords(coordinates, 0)
        has_consecutive_cols = self.check_consecutive_coords(coordinates, 1)

        if not (has_consecutive_rows or has_consecutive_cols):
            print("Error: Ship coordinates must be next to each other.")
            return False
        return True

    def doesnt_overlap_other_ships(self):
        coordinates = self.ship.coordinates
        other_ships = self.other_ships
        ship_name = self.ship.name

        for other_ship in other_ships:
            for coord in coordinates:
                if coord in other_ship.coordinates:
                    print(f"Error: {ship_name} placement overlaps {other_ship.name}.")
                    return False
        return True
