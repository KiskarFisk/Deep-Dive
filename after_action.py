from player_function import player1
import time
import weapon_list as w

def report(level):
    if level == 1:
        player1.tier += 1
    if level == 7:
        print(f"You have gotten {w.pistol.name}, would you like to keep it?")
        if input("Y/N ") == "y":
            player1.replace_weapon(w.pistol)
    if level == 9:
        print(f"C{player1.serial_num}: Where am I going to again?")
        time.sleep(0.5)
        print("HALIDON: Leece. It's in Europe.")
        time.sleep(0.5)
        print("C: And what am I doing there?")
        time.sleep(0.5)
        print("HALIDON: Proving your worth.")
        time.sleep(3)
        player1.tier += 1