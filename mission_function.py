import room_function as room
from player_function import player1
import enemies.tier_1_enemy_list as t1e
import enemies.t2_el as t2e

class Mission:
    def __init__(self, name, type, tier, rooms, ):
        self.name = name
        self.type = type
        self.tier = tier
        self.room_c = rooms
        self.room = 1
        self.etype = self.etype_retrieve()

    def etype_retrieve(self):
        if self.tier == 1:
            return t1e.random_list_t1()
        if self.tier == 2:
            return t2e.random_list()

    def run_mission(self):
        while self.room <= self.room_c:
            self.run_room()
            self.room += 1
        self.complete_mission()

    def run_room(self):
        major = room.Room(self.tier, self.etype)
        major.operate()

    def complete_mission(self):
        print("Congrats, you completed the mission!")
        self.room = 1
        player1.mis_comp += 1 # increments it by 1, thus keeping track of how many missions have been completed

        if player1.objective is not None:
            if self.type == player1.objective.valid_mission_types:
                player1.objective.progress += 1
                if player1.objective.progress <= player1.objective.goal:
                    print("Gained progress toward objective")
                if player1.objective.progress >= player1.objective.goal:
                    player1.objective.progress = player1.objective.goal
                    print("Your objective is complete, please return to the nearest HALIDON Mission Center")