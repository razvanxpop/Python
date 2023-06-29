from exceptions.errors import GridError


class Grid:

    def __init__(self):
        self._grid = [['+---+---+---+---+---+---+---+---+'],
                      ['|   +   +   +   +   +   +   +   |'],
                      ['+---+---+---+---+---+---+---+---+'],
                      ['|   +   +   +   +   +   +   +   |'],
                      ['+---+---+---+---+---+---+---+---+'],
                      ['|   +   +   +   +   +   +   +   |'],
                      ['+---+---+---+---+---+---+---+---+'],
                      ['|   +   +   +   +   +   +   +   |'],
                      ['+---+---+---+---+---+---+---+---+'],
                      ['|   +   +   +   +   +   +   +   |'],
                      ['+---+---+---+---+---+---+---+---+'],
                      ['|   +   +   +   +   +   +   +   |'],
                      ['+---+---+---+---+---+---+---+---+'],
                      ['|   +   +   +   +   +   +   +   |'],
                      ['+---+---+---+---+---+---+---+---+'],
                      ['|   +   +   +   +   +   +   +   |'],
                      ['+---+---+---+---+---+---+---+---+'],
                      ]

    def get_grid(self):
        """Returns the grid"""
        return [grid_row for grid_row in self._grid]

    def add_cell(self, pattern, row, column):
        """Adds an alive cell"""
        if pattern == 'block':
        elif pattern == 'tub':
        elif pattern == 'blinker':
        elif pattern == 'beacon':
        elif pattern == ''
        if self._grid[row][column] == 'X':
            raise GridError("There already exists an alive cell on position", row, ',', column)
        else:
            # adjust input and make move
            row = row + 1
            if column == 1:
                column = column + 1
            else:
                column = 4 * column - 2
            self._grid[row][column] = 'X'

