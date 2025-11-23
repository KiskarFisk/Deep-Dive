#import function
import time
from player_function import player1
import menu_function as menu

#save function

# Game Intro
print(f"You are C{player1.serial_num}.")
time.sleep(0.8)
print("Welcome to the Diver program.")
time.sleep(1)
print("Your goal is to recover materials for the HALIDON corporation.")
time.sleep(1.4)
print("Please do your best, your artificial body is worth $72.")
time.sleep(1.1)

menu.main()
