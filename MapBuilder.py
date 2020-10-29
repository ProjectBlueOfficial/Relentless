from random import random


class Forest:
    def __init__(self):
        self.name = "Forest"
        self.danger = 1
        self.obstruction = 1

    def enter(self):
        print("Entered Forest")

class Mountain:
    def __init__(self):
        self.name = "Mountain"
        self.danger = 5
        self.obstruction = 1

    def enter(self):
        print("Entered Mountain")

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
                if random() <= 0.5:
                    grid[row][col] = Forest()
                else:
                    grid[row][col] = Mountain()
        return grid

    def getGrid(self):
        return self.grid





