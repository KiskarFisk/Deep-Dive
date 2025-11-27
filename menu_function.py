from player_function import player1
import random, time, os
import missions.tier_1_mission_list as t1ml
import save_system as save
import hms as hms

def main():
    print()

    print(f"\nPlease select what to do C{player1.serial_num}")
    print("1. Dive")
    print("2. See Objectives")
    print("3. See your stats")
    print("4. Visit a medpod")
    print("5. Save the game")
    print("6. Visit HALIDON Mission Center")

    player1.energy = player1.energy_max

    inp = input("Choice: ")
    if inp == "1":
        m1 = pull_missions()
        m2 = pull_missions()
        m3 = pull_missions()

        print(f"\n1. {m1.name}")
        print(f"2. {m2.name}")
        print(f"3. {m3.name}")

        inp = input("Choice: ")

        actions = {
            "1": m1.run_mission,
            "2": m2.run_mission,
            "3": m3.run_mission,
        }

        action = actions.get(inp)
        if action:
            action()
        else:
            print("Invalid choice.")

    if inp == "2":
        if player1.objective is not None:
            player1.objective.display_info()
        else:
            print("No objective selected")

    if inp == "3":
        player1.display_info()

    if inp == "4":
        player1.medpod()

    if inp == "5":
        save.save()

    if inp == "6":
        hms.hms_menu()

def pull_missions():
    if player1.rep < 100:
        return random.choice(t1ml.t1_missions)
    elif player1.rep >= 100 and player1.tier == 2:
        return random.choice(t1ml.t1_missions)