class Axis():
    def __init__(self, start, end):
        self.numbers = range(start, end)
        self.markers = [str(_) for _ in self.numbers]

    def __str__(self):
        return ' '.join(self.markers)

    def __getitem__(self, index):
        return self.markers[index]

class NumAxis(Axis):
    def __init__(self, start, end):
        super().__init__(start, end)

    def __str__(self):
        numaxis_str = '  '
        for num in self.numbers:
            if num < 10:
                numaxis_str += f'   {num}'
            else:
                numaxis_str += f'  {num}'
        return numaxis_str

class CharAxis(Axis):
    def __init__(self, start, end):
        super().__init__(start, end)
        self.markers = [chr(_ + 65) for _ in self.numbers]
