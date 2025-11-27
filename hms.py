import random, time
from player_function import player1

def hms_menu():
    print()
    print("HALIDON Mission Center")
    print("1. Turn in mission")
    print("2. Get a new mission")

    inp = input("Choice: ")

    actions = {
        "1": hms_ti_obj,
        "2": hms_g_obj
    }
    action = actions.get(inp)
    if action:
        action()
    else:
        print("Invalid choice.")

def hms_ti_obj():
    if player1.objective is not None:
        if player1.objective.progress == player1.objective.goal:
            print("Thank you for your valiant service!")
            print(f"You have gained {player1.objective.mrew} credits and reputation!")
            player1.credits += player1.objective.mrew
            player1.reputation += player1.objective.rrew
            player1.objective = None
        if player1.objective.progress != player1.objective.goal:
            print("You mission is not complete!")
    else:
        print("You have no mission")

def hms_g_obj():
    if player1.objective is None:
        player1.get_objective()
    else:
        print("You already have a mission!")