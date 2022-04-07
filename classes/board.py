from .ships import *

class Board():
    def __init__(self, player_name, area):
        self.player_name = player_name
        self.area = area
        self.board = [['   ' for i in range(self.area)] for i in range(self.area)]
 
    #  RENDERING THE BOARD
    def row_values_to_string(self, row_values):
        str = ''
        for point in row_values:
            str += f'{point}|'
        return str

    def center_text_on_board(self, text):
        board_length = 4*self.area + 3
        center_point = board_length/2
        indent = int(center_point - len(text)/2)
        return ' ' * indent + text

    def get_centered_board_name(self):
        title = f'{self.player_name.title()}\'s Guesses'
        return self.center_text_on_board(title)

    def get_column_numbers(self):
        col_num_string = ' '
        for i in range(self.area):
            if i < 10:
                col_num_string += f'   {i}'
            else:
                col_num_string += f'  {i}'
        return col_num_string

    def render(self):
        print(self.get_centered_board_name())
        print(self.get_column_numbers())
        for i, row in enumerate(self.board):
            print(f'{chr(i + 65)} |{self.row_values_to_string(row)}')



