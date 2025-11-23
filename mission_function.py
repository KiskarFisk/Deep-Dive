class Mission:
    def __init__(self, name, type, tier, rooms, rtype):
        self.name = name
        self.type = type
        self.tier = tier
        self.room_c = rooms
        self.room = 1
        self.rtype = rtype

    def run_mission(self):
        while self.room <= self.room_c:
            print("temp")
        print("Mission completed!")

    def run_room(self):
        print()