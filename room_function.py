import random
from enemies.tier_1_enemy_list import tier1_enemy_list
from player_function import player1

class Room:
    def __init__(self, tier):
        self.tier = tier

        self.enemy1 = self.get_enemy() # every room will have at least 1 enemy

        self.enemy2 = None
        self.enemy3 = None
        #self.e2decide()

        self.e3decide()

        self.defeated = False

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

    def operate(self):
        operating = True
        while operating:
            self.display_enemies()
            if not self.defeated:
                print("1. Fight")
            print("2. Evacuate")
            if self.defeated:
                print("3. Continue")

            inp = input()
            if inp == "1" and self.defeated == False:
                self.fight()

    def fight(self):
        fight = True
        target = None
        active_enemies = 0
        if self.enemy1 is not None:
            active_enemies += 1
        while active_enemies > 0:
            player1.recover()
            self.display_enemy_detail()
            attacked = False
            while not attacked:
                print("\n1. Attack")
                print("2. Rest")
                inp = input("Choice: ")
                if inp == "1":
                    if self.enemy2 is None and self.enemy3 is None:
                        target = self.enemy1
                    print(f"You have {player1.energy} energy")
                    energy_invest = input("How much energy do you use: ")
                    energy_invest = int(energy_invest)
                    if energy_invest > player1.energy:
                        print("Not enough energy")
                    elif energy_invest <= player1.energy:
                        self.player_attack(target, energy_invest)
                        attacked = True
                if inp == "2":
                    print("You rest, regaining 1 energy")
                    player1.recover()

            if self.enemy1.hp <= 0:
                active_enemies -= 1
        self.defeated = True

    def player_attack(self, target, energy_invest):
        damage = player1.weapon.damage*energy_invest
        target.hp -= damage
        print(f"You dealt {damage} damage to {target.name}")
        player1.energy -= energy_invest

    def display_enemies(self):
        print(self.enemy1.name)
        if self.enemy2 is not None:
            print(self.enemy2.name)

    def display_enemy_detail(self):
        self.enemy1.display_info()
        if self.enemy2 is not None:
            self.enemy2.display_info()