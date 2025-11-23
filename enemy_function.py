import random

class Enemy:
    def __init__(self, name, hp, weapon, energy):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.energy = energy

    def display_info(self):
        print(self.name)
        print(f"HP = {self.hp}")

    def attack(self):
        return self.weapon.damage * random.randint(1, self.energy)