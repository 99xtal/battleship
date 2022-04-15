from .validators import CoordinateValidator

class Prompt:
    def __init__(self, message):
        self.input_message = message
        self.input = None
        self.output = None
        self.prompt()

    def get_raw_input(self):
        self.input = input(self.input_message)
        return self.input

    def prompt(self):
        self.output = self.get_raw_input()

    def get_output(self):
        return self.output

class CoordinatePrompt(Prompt):
    def __init__(self, message):
        super().__init__(message)

    def __repr__(self):
        return f'CoordinatePrompt(\'{self.input}\', {self.output})'

    def prompt(self):
        raw_input = self.get_raw_input()


class CoordinateSetPrompt(Prompt):
    def __init__(self, message):
        super().__init__(message)

    def __repr__(self):
        return f'ExplicitCoordinatePrompt(\'{self.input}\', {self.output})'

    def prompt(self):
        valid_input = self.get_valid_input()
        coordinates = self.generate_coordinates(valid_input)
        self.output = coordinates

    def get_valid_input(self):
        is_valid = False
        while not is_valid:
            raw_input = self.get_raw_input()
            formatted_input = self.format_raw_input(raw_input)
            is_valid = self.check_valid_coordinates(formatted_input)
        return formatted_input

    def format_raw_input(self, raw_input):
        return [str.strip().lower() for str in raw_input.split(',')]

    def generate_coordinates(self, formatted_input):
        grid_index_pairs = self.split_into_grid_indexes(formatted_input)
        return self.format_as_coord_dicts(grid_index_pairs)

    def split_into_grid_indexes(self, str_list):
        return [[ord(str[0])-97, int(str[1:])] for str in str_list]

    def format_as_coord_dicts(self, indexes_list):
        return [{'row': x[0], 'col': x[1]} for x in indexes_list]

    def check_valid_coordinates(self, coordinate_list):
        return all(CoordinateValidator(coord).validate() for coord in coordinate_list)