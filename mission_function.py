import room_function as room
from player_function import player1

class Mission:
    def __init__(self, name, type, tier, rooms, rep_reward, credit_reward):
        self.name = name
        self.type = type
        self.tier = tier
        self.room_c = rooms
        self.room = 1
        self.rep_reward = rep_reward
        self.credit_reward = credit_reward

    def run_mission(self):
        while self.room <= self.room_c:
            self.run_room()
            self.room += 1
        self.complete_mission()

    def run_room(self):
        major = room.Room(self.tier)
        major.operate()

    def complete_mission(self):
        print("Congrats, you completed the mission!")
        player1.rep += self.rep_reward
        print(f"Your reputation increased by {self.rep_reward} and you gained {self.credit_reward} credits")
        player1.credits += self.credit_reward

        if player1.objective is not None:
            if self.type == player1.objective.valid_mission_types:
                player1.objective.progress += 1
                if player1.objective.progress <= player1.objective.goal:
                    print("Gain progress toward objective")
                if player1.objective.progress >= player1.objective.goal:
                    player1.objective.progress = player1.objective.goal
                    print("Your objective is complete, please return to the nearest HALIDON Mission Center")