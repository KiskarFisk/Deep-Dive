import random
import objective_function as obj

class Player:
    def __init__(self):
        self.serial_num = random.randint(99,999999)
        self.objective = random.choice(obj.starter_objectives)

player1 = Player()