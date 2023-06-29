from game.game import Game
from grid.grid import Grid
if __name__ == '__main__':
    grid = Grid()
    game = Game(grid)
    game.play()

