from copy import deepcopy
from math import floor
from random import random
import Locations as l


def getRandomTile():
    tiles = [l.Cave()]
    return deepcopy(tiles[floor(random() * len(tiles))])


class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.generateMap()

    def generateMap(self):
        grid = [None] * self.rows
        for row in range(0, self.rows):
            grid[row] = [None] * self.cols
            for col in range(0, self.cols):
                grid[row][col] = getRandomTile()
        return grid

    def getGrid(self):
        return self.grid
