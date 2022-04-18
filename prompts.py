from validators import CoordinateValidator


class Prompt:
    def __init__(self, message):
        self.input_message = f'{message}\n>>>'
        self.input = None
        self.output = None
        self.validator = None

    def get_valid_input(self):
        """Prompt user input and validate until validation conditions are true"""
        is_valid = False
        while not is_valid:
            raw_input = self._get_raw_input()
            formatted_input = self._format_raw_input(raw_input)
            is_valid = self._check_valid_input(formatted_input)
        return formatted_input

    def _get_raw_input(self):
        self.input = input(self.input_message)
        return self.input

    def _format_raw_input(self, raw_input):
        return [raw_input.strip().lower()]

    def _check_valid_input(self, input_list):
        """Return true if all inputs are valid"""
        return all(self.validator.validate(input) for input in input_list)

    def prompt(self):
        self.output = self._get_raw_input()


class CoordinatePrompt(Prompt):
    """Create a coordinate [x,y] from validated user input"""

    def __init__(self, message):
        super().__init__(message)
        self.validator = CoordinateValidator()

    def __repr__(self):
        return f"CoordinatePrompt('{self.input}', {self.output})"

    def prompt(self):
        valid_input = self.get_valid_input()
        self.output = self.generate_coordinate(valid_input)

    def generate_coordinate(self, coordinate_str):
        """Format raw coordinate string (ex. "a0") into grid readable coordinate (ex. [0,0])"""
        return [ord(coordinate_str[0][0]) - 97, int(coordinate_str[0][1:])]


class CoordinateSetPrompt(CoordinatePrompt):
    """Create a list of coordinates from validated user input"""

    def __init__(self, message):
        super().__init__(message)
        self.validator = CoordinateValidator()

    def __repr__(self):
        return f"ExplicitCoordinatePrompt('{self.input}', {self.output})"

    def prompt(self):
        valid_input = self.get_valid_input()
        self.output = self.generate_coordinates(valid_input)

    def _format_raw_input(self, raw_input):
        """Convert raw input into list of coordinate strings"""
        return [str.strip().lower() for str in raw_input.split(",")]

    def generate_coordinates(self, formatted_input):
        """Format coordinate strings into grid readble coordinates"""
        return [self.generate_coordinate(str) for str in formatted_input]
