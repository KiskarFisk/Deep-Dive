import random
from enemies.tier_1_enemy_list import tier1_enemy_list

class Room:
    def __init__(self, tier):
        self.tier = tier

        self.enemy1 = self.get_enemy() # every room will have at least 1 enemy

        self.e2decide()

        self.e3decide()

    def e2decide(self):
        if self.tier == 1:
            if random.randint(1,100) <= 70: # only a 30% chance at tier 1 of a second enemy
                self.enemy2 = None
            else:
                self.enemy2 = self.get_enemy() #randomize

    def e3decide(self):
        if self.tier == 2: # no third enemy at tier 1
            self.enemy3 = None

    def get_enemy(self):
        if self.tier == 1:
            return random.choice(tier1_enemy_list)

    def debug_room_info(self):
        print(self.enemy1.name)
        if self.enemy2 is not None:
            print(self.enemy2.name)