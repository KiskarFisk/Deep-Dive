class Weapon:
    def __init__(self, name, damage, desc):
        self.name = name
        self.damage = damage
        self.desc = desc

    def display_info(self):
        print(f"{self.name} - {self.damage} damage - priced at: {self.damage/10}\n{self.desc}")