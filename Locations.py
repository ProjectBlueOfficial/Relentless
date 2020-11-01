import Answers as a
import DirectionManager
from Cave import enterCave


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
        else:
            handleResult(result)

class Forest:
    def __init__(self):
        self.name = "Forest"
        self.danger = 1
        self.obstruction = 1

    def enter(self):
        print("Entered Forest")
        DirectionManager.showDirections()

class Mountain:
    def __init__(self):
        self.name = "Mountain"
        self.danger = 5
        self.obstruction = 1

    def enter(self):
        print("Entered Mountain")
        DirectionManager.showDirections()

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
            DirectionManager.enterVillage()
        else:
            handleResult(result)




def handleResult(result):
    if result in a.answersB:
        DirectionManager.showDirections()
    else:
        print("Invalid key.")
        DirectionManager.checkLocations()









