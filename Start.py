import time
import Answers as a
import AbandonedRoad




class Player:
    name = ""
    role = ""
    health = 0
    mana = 0
    sanity = 0
    intelligence = 0
    strength = 0
    gold = 0
    keys = 0
    x = 0
    y = 0

class Warrior(Player):
    role = "Warrior"
    health = 21
    mana = 8
    strength = 6

class Mage(Player):
    role = "Mage"
    health = 11
    mana = 22
    strength = 3

class Marksman(Player):
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
    name = input(">>> ")
    print("Welcome " + name)
    pickClass(name)

def pickClass(name):

    time.sleep(1)
    print("What have you been in the past?"
          "\nA: A Warrior"
          "\nB: A Mage"
          "\nC: A Marksman")
    origin = input(">>> ")
    if origin in a.answersA:
        player = Warrior
    elif origin in a.answersB:
        player = Mage
    elif origin in a.answersC:
        player = Marksman
    else:
        print("Invalid key.")
        pickClass(name)
        return None
    player.name = name
    print(player.name + ", you are a " + player.role)
    AbandonedRoad.init()



if __name__ == '__main__':
    startGame()




