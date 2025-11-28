import random, time
from player_function import player1
import weapon_list as wl
import faction_book as fb

def hms_menu():
    print()
    print("HALIDON Mission Center")
    print("1. Turn in mission")
    print("3. Go to the shop")
    print("4. Faction Dictionary - Warning, contains spoilers")
    print("5. Buy Upgrades")

    inp = input("Choice: ")

    actions = {
        "1": hms_ti_obj,
        "2": hms_shop,
        "3": fb.main,
        "4": hms_upgrade
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
            print(f"You have gained {player1.objective.mrew} credits!")
            player1.credits += player1.objective.mrew
            player1.objective.progress = 0
            player1.objective = None
            player1.tier_up()
            time.sleep(2)
        elif player1.objective.progress != player1.objective.goal:
            print("You mission is not complete!")
    else:
        print("You have no mission")

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

def hms_upgrade():
    options = {
        "1": up_health
    }
    print("1. Upgrade Health (+100 Max HP, 5 Credits)")
    inp = input("Choice: ")
    option = options.get(inp)
    if option:
        option()
    else:
        print("Leaving")

def up_health():
    if player1.credits < 5:
        print("Insufficient Funds")
    else:
        player1.credits -= 5
        player1.max_hp += 100
        player1.hp += 100
        print(f"Max HP is now: {player1.max_hp}")
        time.sleep(2)