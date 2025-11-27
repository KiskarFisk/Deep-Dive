from player_function import player1
import time

def main():
    print("Here you may read about the groups you may come across during your diving.")
    if player1.tier > 0:
        tier1_factions()

def tier1_factions():
    leave = False
    while not leave:
        print("1. The Rats\n"
              "2. Tienne\n"
              "3. Orfast\n"
              "4. New Order Knights\n"
              "5. Toreed Corp.\n"
              "6. HALIDON rebels\n"
              "7. Malbey")
        inp = input("Choice: ")
        options = {
            "1": rat,
            "2": tienne,
            "3": orfast,
            "4": nwo,
            "5": toreed,
            "6": halireb,
            "7": malbey
        }
        option = options.get(inp)
        if option:
            option()
        else:
            print("Leaving")
            leave = True

def rat():
    print("The Rats are a group of drug addicted scavengers, they loot and kill with glee.")
    input("Press enter to continue")
def tienne():
    print("Tienne are a group of mercenaries originating from Old Tokyo. They were once powerful enough to rival HALIDON but the company collapsed after destruction of Japan.")
    input("Press enter to continue")
def orfast():
    print("Orfast is a group operating solely in Terran cities, they're harmless for the most part, when left alone. They fiercely fight for the so-called freedom of humanity on Terra.")
    input("Press enter to continue")
def nwo():
    print("The New Order Knights are a group of fanatic militants. They believe themselves successors of a knightly order, which one they won't tell outsiders. Despite numerous attempts infiltration has proved impossible.")
    input("Press enter to continue")
def toreed():
    print("Toreed Corporation appeared as one of the premier mech and robotics companies. Their initial success was quickly overshadowed by HALIDON.")
    input("Press enter to continue")
def halireb():
    print("Rebels originating from HALIDON, an utter nuisance.")
    input("Press enter to continue")
def malbey():
    print("The Malbey Company was is a frontier exploration company, producing most of their equipment on Terra. Their interests do not align with those of HALIDON.")
    input("Press enter to continue")