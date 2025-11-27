import random, time
from player_function import player1
import weapon_list as wl

def hms_menu():
    print()
    print("HALIDON Mission Center")
    print("1. Turn in mission")
    print("2. Get a new mission")
    print("3. Go to the shop")

    inp = input("Choice: ")

    actions = {
        "1": hms_ti_obj,
        "2": hms_g_obj,
        "3": hms_shop
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

def hms_shop():
    print("Shop rotates after every mission.")
    if player1.last_shop < player1.mis_comp or player1.last_shop == 0:
        player1.last_shop = player1.mis_comp
        player1.shop_inv = []
        for _ in range(3):
            player1.generate_shop()

    for item in player1.shop_inv:
        item.display_info()
        print()

    options = {
        "1": player1.shop_inv[0],
        "2": player1.shop_inv[1],
        "3": player1.shop_inv[2]
    }

    print("Choose an item by typing its corresponding number, 1 being the top. Type anything else to leave.")
    print("Warning, buying a weapon will replace your current one permanently.")
    inp = input("Choice: ")
    option = options.get(inp)
    if option:
        if player1.credits >= option.damage/10:
            player1.replace_weapon(option)
            player1.credits -= option.damage/10
        else:
            print("Insufficient credits")
            time.sleep(2)
    else:
        print("Leaving")
        time.sleep(1)