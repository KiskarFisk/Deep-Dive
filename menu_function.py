from player_function import player1
import random
import missions.tier_1_mission_list as t1ml

def main():
    print(f"\nPlease select what to do C{player1.serial_num}")
    print("1. Dive")
    print("2. See Objectives")

    inp = input("Choice: ")
    if inp == "1":
        m1 = pull_missions()
        m2 = pull_missions()
        m3 = pull_missions()

        print(f"\n1. {m1.name}")
        print(f"2. {m2.name}")
        print(f"3. {m3.name}")

        inp = input("Choice: ")
        if inp == "1":
            m1.run_mission()

    if inp == "2":
        player1.objective.display_info()

def pull_missions():
    return random.choice(t1ml.t1_missions)