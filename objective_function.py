class Objective:
    def __init__(self, name, goal, missions, desc):
        self.name = name
        self.progress = 0
        self.goal = goal
        self.valid_mission_types = missions
        self.desc = desc

    def display_info(self):
        print(f"\n{self.name}")
        print(self.desc)
        print(f"Progress to goal: {self.progress}/{self.goal}")

test_objective = Objective("Test Objective", 3, None, "Test Description")

starter_objectives = [test_objective]