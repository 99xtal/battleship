from axis import CharAxis, NumAxis


class Grid:
    def __init__(self, width, height):
        self.width = width  # x-axis
        self.height = height  # y-axis
        self.y_axis = CharAxis(0, height)
        self.x_axis = NumAxis(0, width)
        self.board_name = None
        self.points = [["   " for _ in range(width)] for _ in range(height)]

    def __repr__(self):
        return f"Grid({self.board_name}, length={self.height}, width = {self.width})"

    def __str__(self):
        return f"{self.board_name}\n{self.x_axis}\n{self.render_grid()}"

    def center(self, text):
        """Center text above grid relative to grid width"""
        board_length = 4 * self.height + 3
        indent = int(board_length / 2 - len(text) / 2)
        return " " * indent + text

    def row_points_to_string(self, row):
        """Create string representation of a row of grid points"""
        return "".join([f"{point}|" for point in row])

    def render_grid(self):
        """Create string representation of grid from points array"""
        points_with_axis = ""
        for i, row in enumerate(self.points):
            points_with_axis += f"{self.y_axis[i]} |{self.row_points_to_string(row)}\n"
        return points_with_axis

    def add_ship(self, ship):
        """Add ship icons to grid at ship coordinates"""
        for coordinate in ship.coordinates:
            self.points[coordinate[0]][coordinate[1]] = ship.icon
        print(self)

    def mark(self, coordinate: list, type: str):
        """Insert attack marker (hit or miss) at center of grid point"""
        target_point = list(self.points[coordinate[0]][coordinate[1]])
        if type == "hit":
            target_point[1] = "X"
        elif type == "miss":
            target_point[1] = "O"
        self.points[coordinate[0]][coordinate[1]] = "".join(target_point)
