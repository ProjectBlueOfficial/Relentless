import time
import Answers as a
import DirectionManager
from Classes import Player, Warrior, Mage, Marksman

player = Player

def startGame():

    print("RELENTLESS")
    pickName()

def pickName():

    time.sleep(0.5)
    print("What is your name?")
    name = input(">>> ")
    print("Welcome " + name)
    pickClass(name)

def pickClass(name):

    time.sleep(0.5)
    print("What have you been in the past?"
          "\nA: A Warrior"
          "\nB: A Mage"
          "\nC: A Marksman")
    origin = input(">>> ")
    if origin in a.answersA:
        player = Warrior()
    elif origin in a.answersB:
        player = Mage()
    elif origin in a.answersC:
        player = Marksman()
    else:
        print("Invalid key.")
        pickClass(name)
        return None
    player.name = name
    print(player.name + ", you are a " + player.role)
    DirectionManager.init()



if __name__ == '__main__':
    startGame()




