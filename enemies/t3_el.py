import weapon_list as w
import enemy_function as enemy
import random

def make_toreed1():
    return enemy.Enemy("Toreed Technician", 80, w.pistol, 1)
def make_toreed2():
    return enemy.Enemy("Toreed Technician", 80, w.auto_pistol, 1)
def make_toreed3():
    return enemy.Enemy("Toreed Transport Bot", 170, w.robo_punch, 1)
def make_toreed4():
    return enemy.Enemy("Toreed Guard", 130, w.rifle, 1)
def make_toreed5():
    return enemy.Enemy("Toreed Guard Robot", 200, w.pistol, 1)
def make_toreed6():
    return enemy.Enemy("Toreed Pilot", 130, w.auto_pistol, 1)

toreed_list = [make_toreed1, make_toreed2, make_toreed3, make_toreed4, make_toreed5, make_toreed6]

t3_list = []

def random_list():
    return random.choice(t3_list)