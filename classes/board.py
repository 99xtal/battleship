from .ships import *

class Board():
    def __init__(self, player_name, area):
        self.player_name = player_name
        self.area = area
        self.board = [['   ' for _ in range(self.area)] for _ in range(self.area)]
 
    def row_values_to_string(self, row_values):
        formatted_row_values = [f'{point}|' for point in row_values]
        return ''.join(formatted_row_values)

    def center_text_on_board(self, text):
        board_length = 4*self.area + 3
        indent = int(board_length/2 - len(text)/2)
        return ' ' * indent + text

    def print_board_name(self):
        title = f'{self.player_name.title()}\'s Guesses'
        print(self.center_text_on_board(title))

    def print_column_numbers(self):
        formatted_col_nums = [f'   {i}' if i<10 else f'  {i}' for i in range(self.area)]
        print(' ' + ''.join(formatted_col_nums))

    def render(self):
        self.print_board_name()
        self.print_column_numbers()
        for i, row in enumerate(self.board):
            print(f'{chr(i + 65)} |{self.row_values_to_string(row)}')