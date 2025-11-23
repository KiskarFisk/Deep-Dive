import random

class Room:
    def __init__(self, tier):
        self.enemy1 = None # every room will have at least 1 enemy

        self.e2decide()

        self.e3decide()
        self.enemy3 = None

        self.tier = tier

    def e2decide(self):
        if self.tier == 1:
            if random.randint(1,100) <= 70: # only a 30% chance at tier 1 of a second enemy
                self.enemy2 = None
            else:
                self.enemy2 = None #randomize

    def e3decide(self):
        if self.tier == 2: # no third enemy at tier 1
            self.enemy3 = None