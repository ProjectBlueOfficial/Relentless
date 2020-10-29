import time
from math import floor

import Combat

import Answers as a
from Enemy import Zombie
from MapBuilder import Map
from Start import player
import Strings as s

map = Map(10, 10)

def init():
    time.sleep(1)
    player.x = floor(map.rows / 2)
    player.y = floor(map.cols / 2)
    print("You wake up on an abandoned street... Where do you go next?"
          "\nA: North"
          "\nB: East"
          "\nC: South"
          "\nD: West")
    direction = input(">>> ")
    movePlayer(direction)


def checkLocations():
    time.sleep(1)
    elif player.x == 5 and player.y == 5:
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
    else:
        showDirections()


def showDirections():
    print("There is nothing around you... Where do you go next?")
    if player.y < map.rows:
        print("A: North")
    if player.x < map.cols:
        print("B: East")
    if player.y > 1:
        print("C: South")
    if player.x > 1:
        print("D: West")
    direction = input(">>> ")
    movePlayer(direction)


def movePlayer(direction):
    if direction in a.answersA:
        if player.y == map.rows:
            print("You can not go here.")
            checkLocations()
        else:
            goNorth()
    elif direction in a.answersB:
        if player.x == map.cols:
            print("You can not go here.")
            checkLocations()
        else:
            goEast()
    elif direction in a.answersC:
        if player.y == 1:
            print("You can not go here.")
            checkLocations()
        else:
            goSouth()
    elif direction in a.answersD:
        if player.x == 1:
            print("You can not go here.")
            checkLocations()
        else:
            goWest()
    else:
        print("Invalid key.")
        checkLocations()


def goNorth():
    player.y += 1
    checkLocations()


def goWest():
    player.x -= 1
    checkLocations()


def goSouth():
    player.y -= 1
    checkLocations()


def goEast():
    player.x += 1
    checkLocations()


def enterVillage():
    time.sleep(1)
    print("You entered the village.")


def enterCave():
    time.sleep(1)
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
    time.sleep(1)
    print("A Zombie approaches! What do you do?"
          "\nA: Fight!"
          "\nB: Flee")
    result = input(">>> ")
    if result in a.answersA:
        setupBattle()
    elif result in a.answersB:
        if Combat.flee():
            exitCave()
        else:
            setupBattle()
    else:
        print("Invalid key.")
    goDeeper()




def setupBattle():
    time.sleep(1)
    enemy = Zombie
    showBattle(enemy)

def showBattle(enemy):
    print("You stand in front of a " + enemy.name + ". What do you do?"
                                                    "\nA: Attack"
                                                    "\nB: Parry"
                                                    "\nC: Item"
                                                    "\nD: Flee")
    result = input(">>> ")
    if result in a.answersA:
        if Combat.attack(player, enemy) == s.KILL:
            exitCave()
            return None
        elif Combat.attack(player, enemy) == s.DEATH:
            exitGame()
            return None
    elif result in a.answersB:
        Combat.parry(enemy)
    elif result in a.answersC:
        Combat.useItem(enemy)
    elif result in a.answersD:
        Combat.flee()
    else:
        print("Invalid key.")
        showBattle(enemy)
    Combat.enemyTurn(enemy)

def exitCave():
    time.sleep(1)
    print("You left the cave.")
    showDirections()

def exitGame():
    print("You tried, but did not stand the test of time. May you be blessed with better luck next time.")








