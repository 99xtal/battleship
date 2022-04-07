from .board import Board

class ShipBoard(Board):
    def __init__(self, player_name, area):
        super().__init__(player_name, area)

    def get_centered_board_name(self):
        title = f'{self.player_name.title()}\'s Ships'
        return self.center_text_on_board(title)

    def add_ship(self, ship):
        for coord in ship.coordinates:
            self.board[coord[0]][coord[1]] = ship.icon

  