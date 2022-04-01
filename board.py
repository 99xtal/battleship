class Board():
    def __init__(self):
        self.board = {
        'A': ['   '] * 20,
        'B': ['   '] * 20,
        'C': ['   '] * 20,
        'D': ['   '] * 20,
        'E': ['   '] * 20,
        'F': ['   '] * 20,
        'G': ['   '] * 20,
        'H': ['   '] * 20,
        'I': ['   '] * 20,
        'J': ['   '] * 20,
        'K': ['   '] * 20,
        'L': ['   '] * 20,
        'M': ['   '] * 20,
        'N': ['   '] * 20,
        'O': ['   '] * 20,
        'P': ['   '] * 20,
        'Q': ['   '] * 20,
        'R': ['   '] * 20,
        'S': ['   '] * 20,
        'T': ['   '] * 20,
        }
    
    def display_board(self):
        board = self.board
        row_letters = list(self.board)
        print('    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19')
        for i in range(len(self.board)):
            print(f'{row_letters[i]} |{self.row_values_to_string(board[row_letters[i]])}')

    def row_values_to_string(self, row_values):
        str = ''
        for point in row_values:
            str += f'{point}|'
        return str

    def mark(self, coordinate_str, type):
        row, col = self.str_to_coordinate(coordinate_str)
        if type.lower() == 'hit':
            self.board[row][col] = ' X '
        elif type.lower() == 'miss':
            self.board[row][col] = ' O '

    def str_to_coordinate(self, str):
        row = str[0].upper()
        col = int(str[1:])
        return row, col


testing_board = Board()
testing_board.mark('b3','hit')
testing_board.mark('f11','miss')
testing_board.mark('t19','hit')
testing_board.display_board()
