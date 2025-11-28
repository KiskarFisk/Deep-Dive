import random, time, os
import weapon_list as wl
import objectives.tier_1_objective_list as obj1
import objectives.t2_ol as obj2

class Player:
    def __init__(self):
        self.serial_num = random.randint(99,999999)
        self.objective = None

        self.hp = 600
        self.max_hp = 600
        self.rep = 0
        self.credits = 5
        self.energy = 5
        self.energy_max = 5

        self.augments = 0
        self.max_augments = 1

        self.last_shop = 0
        self.mis_comp = 0
        self.shop_inv = []

        self.tier = 0
        self.current_mission = 1

        self.weapon = wl.machete

    def dieded(self):
        dead = True
        while dead:
            print("You have died. Please quit the game.")
            time.sleep(99999999) # temporary measure since this was pissing me off

    def recover(self):
        if self.energy < self.energy_max:
            self.energy += 1

    def medpod(self):
        print(f"You have {self.hp}/{self.max_hp} HP and {self.credits} credits - It costs 1 credit per 100 HP recovered")
        inp = input("How many credits will you spend? ")
        inp = int(inp)
        if inp > self.credits:
            print("Insufficient funds")
        else:
            self.hp += 100 * inp
            self.credits -= inp
            if self.hp > self.max_hp:
                self.hp = self.max_hp
                print("Recovered to full HP")
            else:
                print(f"Recovered {inp*100} HP")

    def display_info(self):
        print(f"\nYou have {self.hp}/{self.max_hp} HP and {self.energy}/{self.energy_max} energy")
        print(f"{self.credits} Credits")
        self.weapon.display_info()
        time.sleep(1)

    def replace_weapon(self, weapon):
        self.weapon = weapon

    def generate_shop(self):
        if self.tier == 1:
            self.shop_inv.append(random.choice(wl.t1_shop_list))
        if self.tier == 2:
            self.shop_inv.append(random.choice(wl.t2_shop_list))
        if self.tier == 3:
            self.shop_inv.append(random.choice(wl.t3_shop_list))

    def tier_up(self):
        if self.tier == 1 and self.rep >= 100:
            self.tier = 2
            print("You have achieved TIER II")
        if self.tier == 2 and self.rep >= 300:
            self.tier = 3
            print("You have achieved TIER III")

player1 = Player()