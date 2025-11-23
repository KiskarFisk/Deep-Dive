from player_function import player1
import random

def main():
    print(f"\nPlease select what to do C{player1.serial_num}")
    print("1. Dive")
    print("2. See Objectives")

    inp = input("Choice: ")
    if inp == "1":
        print()
    if inp == "2":
        player1.objective.display_info()