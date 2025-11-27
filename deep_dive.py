#import function
import time, os
from player_function import player1
import menu_function as menu
import save_system as save

skip_intro = False

def extra_load():
    if os.path.exists("save_data.pkl"):
        save.load()
        do_the_thing()
    else:
        print("No save exists, reloading the game.")
        do_the_thing()

#save function
if os.path.exists("save_data.pkl"):
    inp = input("y/n load existing save? ")
    if inp == "y":
        save.load()
        skip_intro = True
    else:
        print("Not loading save, good luck!")

# Game Intro
if skip_intro is False:
    print(f"You are C{player1.serial_num}.")
    time.sleep(0.8)
    print("Welcome to the Diver program.")
    time.sleep(1)
    print("Your goal is to recover materials for the HALIDON corporation.")
    time.sleep(1.4)
    print("Please do your best, your artificial body is worth $72.")
    time.sleep(1.1)

def do_the_thing():
    menu.main()

while True:
    do_the_thing()