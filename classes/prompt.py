

class Prompt:
    def __init__(self):
        self.input = None
        self.output = None

class CoordinatePrompt(Prompt):
    def __init__(self, ship):
        super().__init__()
        self.input_message = f'Please enter ({ship.length}) coordinates for your {ship.name} (separated by commas)\n>>>'
        self.output = None

        self.prompt()

    def __repr__(self):
        return f'ExplicitCoordinatePrompt(\'{self.input}\', {self.output})'

    def prompt(self):
        raw_input = self.get_raw_input()
        formatted_input = self.format_raw_input(raw_input)
        coordinates = self.generate_coordinates(formatted_input)
        self.output = coordinates

    def get_raw_input(self):
        return input(self.input_message).lower()

    def format_raw_input(self, raw_input):
        return [str.strip() for str in raw_input.split(',')]

    def generate_coordinates(self, formatted_input):
        grid_index_pairs = self.split_into_grid_indexes(formatted_input)
        return self.format_as_coord_dicts(grid_index_pairs)

    def split_into_grid_indexes(self, str_list):
        return [[ord(str[0])-97, int(str[1:])] for str in str_list]

    def format_as_coord_dicts(self, indexes_list):
        return [{'row': x[0], 'col': x[1]} for x in indexes_list]

    def get_output(self):
        return self.output

    # def generate_coordinate_set(self):
    #     while(True):
    #         self.get_input()
    #         try:
    #             input_str_list = self.format_input_to_list()
    #             coordinate_indexes = self.split_into_indexes(input_str_list)
    #             coordinates = self.format_as_coord_dicts(coordinate_indexes)
    #         except ValueError:
    #             print('Bad Input: Please try again')
    #         else:
    #             self.output = coordinates
    #             break

    def output(self):
        return self.output
