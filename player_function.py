import random, time
import objective_function as obj
import weapon_list as wl

class Player:
    def __init__(self):
        self.serial_num = random.randint(99,999999)
        self.objective = random.choice(obj.starter_objectives)

        self.hp = 600
        self.max_hp = 600
        self.rep = 0
        self.energy = 5
        self.energy_max = 5

        self.weapon = wl.machete

    def recover(self):
        if self.energy < self.energy_max:
            self.energy += 1

    def display_info(self):
        print(f"You have {self.hp}/{self.max_hp} HP and {self.energy}/{self.energy_max} energy")
        self.weapon.display_info()
        time.sleep(1)

player1 = Player()