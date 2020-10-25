import time
from random import random
import Strings as s
import AbandonedRoad
from Start import player


def attack(caster, target):
    if random() <= 0.1:
        print("That attack missed!")
        return s.MISS
    if random() >= 0.9:
        print("A critical hit!")
        damage = caster.strength * 1.5
    else:
        damage = caster.strength

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
    if attack(enemy, player) == s.KILL:
        AbandonedRoad.exitGame()
    elif attack(enemy, player) == s.DEATH:
        AbandonedRoad.exitCave()
    AbandonedRoad.showBattle(enemy)

def flee():
    time.sleep(1)
    if random() >= 0.5:
        print("Fleeing successful.")
        return True
    else:
        print("Fleeing failed, you are being attacked!")
        return False
