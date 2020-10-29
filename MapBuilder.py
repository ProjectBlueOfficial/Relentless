from random import random

import Answers as a
from AbandonedRoad import checkLocations, showDirections, enterVillage, enterCave


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

class Village:
    def __init__(self):
        self.name = "Village"
        self.danger = 0
        self.obstruction = 0

    def enter(self):
        print("You can see a village from a far... Approach it?"
              "\nA: Yes"
              "\nB: No")
        result = input(">>> ")
        if result in a.answersA:
            enterVillage()
        elif result in a.answersB:
            showDirections()
        else:
            print("Invalid key.")
            checkLocations()

class Cave:
    def __init__(self):
        self.name = "Cave"
        self.danger = 0
        self.obstruction = 0

    def enter(self):
        print("You can see the entrance to a cave... Enter it?"
              "\nA: Yes"
              "\nB: No")
        result = input(">>> ")
        if result in a.answersA:
            enterCave()
        elif result in a.answersB:
            showDirections()
        else:
            print("Invalid key.")
            checkLocations()

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





