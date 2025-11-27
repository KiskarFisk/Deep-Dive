class Objective:
    def __init__(self, name, goal, missions, desc, mrew, rrew):
        self.name = name
        self.progress = 0
        self.goal = goal
        self.valid_mission_types = missions
        self.desc = desc
        self.mrew = mrew
        self.rrew = rrew

    def display_info(self):
        print(f"\n{self.name}")
        print(self.desc)
        print(f"Progress to goal: {self.progress}/{self.goal}")

scav1 = Objective("Scavenge Old Equipment", 3, "scavenge",
                           "A HALIDON tech team needs some materials to be scavenged from some local sites.", 5, 40)

starter_objectives = [scav1]