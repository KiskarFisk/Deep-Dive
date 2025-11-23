from player_function import player1
import random, time
import missions.tier_1_mission_list as t1ml

def main():
    print(f"\nPlease select what to do C{player1.serial_num}")
    print("1. Dive")
    print("2. See Objectives")
    print("3. See your info")

    # temporary code
    player1.hp = player1.max_hp

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
            m2.run_mission()
        if inp == "3":
            m3.run_mission()

    if inp == "2":
        player1.objective.display_info()

    if inp == "3":
        player1.display_info()

def pull_missions():
    return random.choice(t1ml.t1_missions)