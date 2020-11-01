import time
from math import floor
from random import random
import Strings as s
import DirectionManager
import Cave
from Enemy import Zombie
import Start
import Answers as a



def setupBattle():
    time.sleep(0.5)
    enemy = Zombie
    showBattle(enemy)

def showBattle(enemy):
    print("You stand in front of a " + enemy.name + ". What do you do?" +
          "\nA: Attack"
          "\nB: Parry"
          "\nC: Item"
          "\nD: Flee")
    result = input(">>> ")
    if result in a.answersA:
        attackResult = attack(Start.player, enemy)
        if attackResult == s.KILL:
            Cave.exitCave()
            return None
        elif attackResult == s.DEATH:
            DirectionManager.exitGame()
            return None
    elif result in a.answersB:
        parry(enemy)
    elif result in a.answersC:
        useItem(enemy)
    elif result in a.answersD:
        flee()
    else:
        print("Invalid key.")
        showBattle(enemy)
        return None
    enemyTurn(enemy)

def attack(caster, target):
    damageModifier = 1
    if random() <= 0.1:
        print("That attack missed!")
        return s.MISS
    if random() >= 0.9:
        print("A critical hit!")
        damageModifier = 1.5
    damage = floor(caster.strength * damageModifier)
    print(caster.name + " attacked " + target.name + " for " + str(damage) + " damage!")
    target.health -= damage
    if target.health <= 0:
        print(target.name + " has been killed!")
        if target.health <= 0:
            return s.DEATH
        else:
            return s.KILL
    else:
        return s.HIT


def enemyTurn(enemy):
    result = attack(enemy, Start.player)
    if result == s.KILL:
        DirectionManager.exitGame()
    elif result == s.DEATH:
        Cave.exitCave()
    showBattle(enemy)

def flee():
    time.sleep(0.5)
    if random() >= 0.5:
        print("Fleeing successful.")
        return True
    else:
        print("Fleeing failed, you are being attacked!")
        return False


def parry(enemy):
    return None


def useItem(enemy):
    return None