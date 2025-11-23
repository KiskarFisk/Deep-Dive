import random
import objective_function as obj
import weapon_list as wl

class Player:
    def __init__(self):
        self.serial_num = random.randint(99,999999)
        self.objective = random.choice(obj.starter_objectives)

        self.hp = 600

        self.weapon = wl.machete

player1 = Player()