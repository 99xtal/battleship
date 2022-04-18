from validators import CoordinateValidator

class Prompt:
    def __init__(self, message):
        self.input_message = message
        self.input = None
        self.output = None
        self.validator = None

    def get_raw_input(self):
        self.input = input(self.input_message)
        return self.input

    def format_raw_input(self, raw_input):
        return [raw_input.strip().lower()]

    def get_valid_input(self):
        is_valid = False
        while not is_valid:
            raw_input = self.get_raw_input()
            formatted_input = self.format_raw_input(raw_input)
            is_valid = self.check_valid_input(formatted_input)
        return formatted_input

    def check_valid_input(self, input_list):
        return all(self.validator.validate(input) for input in input_list)

    def prompt(self):
        self.output = self.get_raw_input()

    def get_output(self):
        return self.output

class CoordinatePrompt(Prompt):
    def __init__(self, message):
        super().__init__(message)
        self.validator = CoordinateValidator()

    def __repr__(self):
        return f'CoordinatePrompt(\'{self.input}\', {self.output})'

    def prompt(self):
        valid_input = self.get_valid_input()
        self.output = self.generate_coordinate(valid_input)

    def generate_coordinate(self, str):
        grid_indexes = [ord(str[0])-97, int(str[1:])]
        return {'row': grid_indexes[0], 'col': grid_indexes[1]}


class CoordinateSetPrompt(CoordinatePrompt):
    def __init__(self, message):
        super().__init__(message)
        self.validator = CoordinateValidator()

    def __repr__(self):
        return f'ExplicitCoordinatePrompt(\'{self.input}\', {self.output})'

    def prompt(self):
        valid_input = self.get_valid_input()
        self.output = self.generate_coordinates(valid_input)

    def format_raw_input(self, raw_input):
        return [str.strip().lower() for str in raw_input.split(',')]

    def generate_coordinates(self, formatted_input):
        return [self.generate_coordinate(str) for str in formatted_input]


