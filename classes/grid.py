from .axis import CharAxis, NumAxis

class Grid():
    def __init__(self, board_name, length, width):
        self.board_name = board_name
        self.length = length
        self.width = width
        self.letter_axis = CharAxis(0, length)
        self.number_axis = NumAxis(0, width)
        self.points = [['   ' for _ in range(width)] for _ in range(length)]

    def __repr__(self):
        return f'Grid({self.board_name}, length={self.length}, width = {self.width})'

    def __str__(self):
        return self.assemble_grid()

    def center(self, str):
        board_length = 4*self.length + 3
        indent = int(board_length/2 - len(str)/2)
        return ' ' * indent + str

    def row_points_to_string(self, row):
        formatted_grid_point_strs = [f'{point}|' for point in row]
        return ''.join(formatted_grid_point_strs)

    def join_points_with_axis(self):
        points_with_axis = ''
        for i, row in enumerate(self.points):
            points_with_axis += f'{self.letter_axis[i]} |{self.row_points_to_string(row)}\n'
        return points_with_axis

    def assemble_grid(self):
        board_name = self.center(self.board_name)
        number_axis = self.number_axis
        points_with_letter_axis = self.join_points_with_axis()
        
        return f'{board_name}\n{number_axis}\n{points_with_letter_axis}'

    # def add_ships(self):
    #     print(self.grid)
    #     for ship in self.ships:
    #         is_valid = False
    #         while not is_valid:
    #             ship.set_coordinates()
    #             is_valid = True
    #             # is_valid = ShipPlacementValidator.validate()
    #             if is_valid:
    #                 self.add_ship_to_board()
    #                 print(self.grid)