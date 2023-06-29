class Game:

    def __init__(self, grid):
        self.__grid = grid

    def __display_grid(self):
        """Prints the grid"""
        print(*self.__grid.get_grid(), sep='\n')

    def play(self):
        """Starts the game"""
        self.__display_grid()
        while True:
            pass
