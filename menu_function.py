from player_function import player1
import random, time, os
import missions.tier_1_mission_list as t1ml
import missions.t2_ml as t2ml
import missions.t3_ml as t3ml
import save_system as save
import hms as hms
import missions.story_missions as stor
from colorama import Fore, Style

def main():
    print()
    player1.hp = player1.max_hp

    print(f"\nPlease select what to do C{player1.serial_num}")
    print("1. Dive")
    print("2. See Objectives")
    print("3. See your stats")
    print("4. Visit a medpod")
    print("5. Save the game")
    print("6. Use Your HALIDON Mobile Computer")

    player1.energy = player1.energy_max

    inp = input("Choice: ")
    if inp == "1":
        m1 = get_story_mission()
        m2 = pull_missions()
        m3 = pull_missions()

        if not m1:
            print("1. UNAVAILABLE")
        else:
            print(Fore.BLUE + f"\n1. {m1.name}" + Style.RESET_ALL)
        if m2 == None:
            print("2. UNAVAILABLE")
        else:
            print(f"2. {m2.name}")

        if m3 == None:
            print("3. UNAVAILABLE")
        else:
            print(f"3. {m3.name}")

        inp = input("Choice: ")

        actions = {
            "1": m1.run_mission if m1 else None, # Will now always be a STORY mission
            "2": m2.run_mission if m2 else None,
            "3": m3.run_mission if m3 else None,
        }

        action = actions.get(inp)
        if action:
            action()
        else:
            print("Invalid choice.")

    if inp == "2":
        if player1.objective is not None:
            player1.objective.display_info()
            input("Press enter to continue")
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
    if player1.tier == 0:
        return None
    if player1.tier == 1:
        return random.choice(t1ml.t1_missions)
    elif player1.tier == 2:
        return random.choice(t2ml.t2_misslist)
    elif player1.tier == 3:
        return random.choice(t3ml.t3_mlist)

def get_story_mission():
    return stor.get_mission()