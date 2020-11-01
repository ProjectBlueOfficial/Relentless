import time

import Answers as a
import Combat
import DirectionManager




def enterCave():
    time.sleep(0.5)
    print("You entered the cave. The darkness prevents you from seeing your surroundings. Move on?"
          "\nA: Yes"
          "\nB: No")
    result = input(">>> ")
    if result in a.answersA:
        goDeeper()
    elif result in a.answersB:
        exitCave()
    else:
        print("Invalid key.")
    enterCave()


def goDeeper():
    time.sleep(0.5)
    print("A Zombie approaches! What do you do?"
          "\nA: Fight!"
          "\nB: Flee")
    result = input(">>> ")
    if result in a.answersA:
        Combat.setupBattle()
    elif result in a.answersB:
        if Combat.flee():
            exitCave()
        else:
            Combat.setupBattle()
    else:
        print("Invalid key.")
        goDeeper()

def exitCave():
    time.sleep(0.5)
    print("You left the cave.")
    DirectionManager.showDirections()