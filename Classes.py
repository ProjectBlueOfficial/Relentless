



class Player:
    def __init__(self):
        self.name = ""
        self.role = ""
        self.health = 0
        self.mana = 0
        self.strength = 0
        self.intelligence = 0
        self.sanity = 0
        self.gold = 0
        self.keys = 0
        self.x = 0
        self.y = 0

class Warrior(Player):
    def __init__(self):
        super().__init__()
        self.role = "Warrior"
        self.health = 21
        self.mana = 9
        self.strength = 7
        self.intelligence = 2

class Mage(Player):
    def __init__(self):
        super().__init__()
        self.role = "Mage"
        self.health = 13
        self.mana = 22
        self.strength = 3
        self.intelligence = 8

class Marksman(Player):
    def __init__(self):
        super().__init__()
        self.role = "Marksman"
        self.health = 16
        self.mana = 14
        self.strength = 5
        self.intelligence = 4
