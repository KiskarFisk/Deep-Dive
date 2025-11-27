import random, time, os
import enemies.tier_1_enemy_list as t1e
import enemies.t2_el as t2e
import enemies.t3_el as t3e
from player_function import player1

class Room:
    def __init__(self, tier, elist):
        self.tier = tier
        self.etype = elist

        self.enemy1 = self.get_enemy() # every room will have at least 1 enemy

        self.enemy3 = None
        self.e2decide()

        self.e3decide()

        self.defeated = False

    def e2decide(self):
        if self.tier == 1:
            if random.randint(1,100) <= 70: # only a 30% chance at tier 1 of a second enemy
                self.enemy2 = None
            else:
                self.enemy2 = self.get_enemy() #randomize
        if self.tier == 2:
            if random.randint(1,100) <= 66: # 1/3
                self.enemy2 = None
            else:
                self.enemy2 = self.get_enemy()
        if self.tier == 3:
            if random.randint(1,100) <= 40: #60%
                self.enemy2 = None
            else:
                self.enemy2 = self.get_enemy

    def e3decide(self):
        if self.tier == 1: # no third enemy at tier 1
            self.enemy3 = None
        if self.enemy2 is not None:
            if self.tier == 2:
                if random.randint(1,100) <= 70: # 30%
                    self.enemy3 = None
                else:
                    self.enemy3 = self.get_enemy()
            if self.tier == 3:
                if random.randint(1,100) <= 60: # 40%
                    self.enemy3 = None
                else:
                    self.enemy3 = self.get_enemy()

    def get_enemy(self):
        if self.tier == 1:
            enemy_class = t1e.enemy_retrieve(self.etype)
            enemy_instance = enemy_class()
            return enemy_instance
        if self.tier == 2:
            enemy_class = t2e.enemy_retrieve(self.etype)
            enemy_instance = enemy_class()
            return enemy_instance
        if self.tier == 3:
            enemy_class = t3e.enemy_retrieve(self.etype)
            enemy_instance = enemy_class()
            return enemy_instance

    def operate(self):
        operating = True
        while operating:
            print()
            self.display_enemies()
            if not self.defeated:
                print("1. Fight")
            print("2. Evacuate")
            if self.defeated:
                print("3. Continue")
            print("4. View your stats")

            inp = input("Choice: ")
            if inp == "1" and self.defeated == False:
                self.fight()

            if inp =="3" and self.defeated:
                operating = False

            if inp == "4":
                player1.display_info()

    def fight(self):
        fight = True
        target = None
        active_enemies = 0
        if self.enemy1 is not None:
            active_enemies += 1
        if self.enemy2 is not None:
            active_enemies += 1
        if self.enemy3 is not None:
            active_enemies += 1
        while active_enemies > 0 and player1.hp > 0:
            player1.recover()
            self.display_enemy_detail()
            attacked = False
            while not attacked:
                print("\n1. Attack")
                print("2. Rest")
                print("3. See your info")
                inp = input("Choice: ")
                if inp == "1":
                    if self.enemy2 is None and self.enemy3 is None:
                        target = self.enemy1
                    if self.enemy1 is None and self.enemy3 is None:
                        target = self.enemy2
                    if self.enemy1 is None and self.enemy2 is None:
                        target = self.enemy3
                    if active_enemies > 1:
                        print("1-3 to select an enemy to attack")
                        inp = input("Choice: ")
                        if inp == "1" and self.enemy1 is not None:
                            target = self.enemy1
                        if inp == "2" and self.enemy2 is not None:
                            target = self.enemy2
                        if inp == "3" and self.enemy3 is not None:
                            target = self.enemy3
                    inp = 0
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
                    attacked = True

                if inp == "3":
                    player1.display_info()

            if self.enemy1:
                if self.enemy1.hp <= 0:
                    active_enemies -= 1
                    print(f"You defeated {self.enemy1.name}")
                    self.enemy1 = None
            if self.enemy2:
                if self.enemy2.hp <= 0:
                    active_enemies -= 1
                    print(f"You defeated {self.enemy2.name}")
                    self.enemy2 = None
            if self.enemy3:
                if self.enemy3.hp <= 0:
                    active_enemies -= 1
                    print(f"You defeated {self.enemy3.name}")
                    self.enemy3 = None

            if active_enemies > 0:
                self.enemy_attacks()
        self.defeated = True
        if player1.hp <= 0:
            player1.dieded()

    def player_attack(self, target, energy_invest):
        damage = player1.weapon.damage*energy_invest
        target.hp -= damage
        print(f"You dealt {damage} damage to {target.name}")
        player1.energy -= energy_invest

    def enemy_attacks(self):
        enemies = [self.enemy1, self.enemy2, self.enemy3]
        for enemy in enemies:
            if enemy is not None:
                damage = enemy.attack()
                print(f"You take {damage} damage from {enemy.name}'s {enemy.weapon.name}!")
                player1.hp -= damage
                time.sleep(1)

    def display_enemies(self):
        if self.enemy1:
            print(self.enemy1.name)
        if self.enemy2:
            print(self.enemy2.name)
        if self.enemy3:
            print(self.enemy3.name)

    def display_enemy_detail(self):
        if self.enemy1:
            self.enemy1.display_info()
        if self.enemy2 is not None:
            self.enemy2.display_info()
        if self.enemy3 is not None:
            self.enemy3.display_info()