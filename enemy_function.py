class Enemy:
    def __init__(self, name, hp, weapon):
        self.name = name
        self.hp = hp
        self.weapon = weapon

    def display_info(self):
        print(self.name)
        print(f"HP = {self.hp}")