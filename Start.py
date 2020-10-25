import time
import Answers as a
import AbandonedRoad


class Player:
    role = None
    health = 0
    mana = 0
    strength = 0
    keys = 0
    x = 3
    y = 3


class Warrior:
    role = "Warrior"
    health = 21
    mana = 8
    strength = 6

class Mage:
    role = "Mage"
    health = 11
    mana = 22
    strength = 3

class Marksman:
    role = "Marksman"
    health = 15
    mana = 12
    strength = 7


player = Player


def startGame():

    print("RELENTNESS")
    pickName()

def pickName():

    time.sleep(1)
    print("What is your name?")
    player.name = input(">>> ")
    print("Welcome " + player.name)
    pickClass()

def pickClass():

    time.sleep(1)
    print("What have you been in the past?"
          "\nA: A Warrior"
          "\nB: A Mage"
          "\nC: A Marksman")
    origin = input(">>> ")
    tempName = player.name
    if origin in a.answersA:
        player = Warrior
    elif origin in a.answersB:
        player = Mage
    elif origin in a.answersC:
        player = Marksman
    else:
        print("Invalid key.")
        pickClass(player)
    player.name = tempName
    print(player.name + ", you are a " + player.role)
    AbandonedRoad.init()



if __name__ == '__main__':
    startGame()




