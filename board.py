from ships import *

class Board():
    def __init__(self, area):
        self.area = area
        self.board = [['   ' for i in range(self.area)] for i in range(self.area)]
 
    #  RENDERING THE BOARD

    def row_values_to_string(self, row_values):
        str = ''
        for point in row_values:
            str += f'{point}|'
        return str    

    def render(self):
        print('    0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19')
        
        for row in self.board:
            print(row)

test = Board(20)
