import time
from math import floor

import Answers as a
from MapBuilder import Map
from Start import player

map = Map(10, 10)


def init():
    time.sleep(0.5)
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
    time.sleep(0.5)
    map.getGrid()[player.x][player.y].enter()


def showDirections():
    time.sleep(0.5)
    print("There is nothing around you... Where do you go next?")
    if player.y < map.rows - 1:
        print("A: North")
    if player.x < map.cols - 1:
        print("B: East")
    if player.y > 0:
        print("C: South")
    if player.x > 0:
        print("D: West")
    direction = input(">>> ")
    movePlayer(direction)


def movePlayer(direction):
    if direction in a.answersA:
        if player.y == map.rows - 1:
            print("You can not go here.")
            checkLocations()
        else:
            goNorth()
    elif direction in a.answersB:
        if player.x == map.cols - 1:
            print("You can not go here.")
            checkLocations()
        else:
            goEast()
    elif direction in a.answersC:
        if player.y == 0:
            print("You can not go here.")
            checkLocations()
        else:
            goSouth()
    elif direction in a.answersD:
        if player.x == 0:
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
    time.sleep(0.5)
    print("You entered the village.")

def exitGame():
    print("You tried, but did not stand the test of time. May you be blessed with better luck next time.")
