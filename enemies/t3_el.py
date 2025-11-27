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
def make_toreed7():
    return enemy.Enemy("Toreed Micro Mech", 200, w.mech_pistol, 1)

def make_halireb1():
    return enemy.Enemy("HALIDON Rebel Scientist", 100, w.auto_pistol, 1)
def make_halireb2():
    return enemy.Enemy("HALIDON Rebel Guard", 140, w.rifle, 1)
def make_halireb3():
    return enemy.Enemy("HALIDON Rebel Soldier", 160, w.rifle, 1)
def make_halireb4():
    return enemy.Enemy("HALIDON Rebel Soldier", 160, w.mk1_laz_pistol, 1)

def make_malbey1():
    return enemy.Enemy("Malbey Technician", 100, w.auto_pistol, 1)
def make_malbey2():
    return enemy.Enemy("Malbey Guard", 160, w.rifle, 1)
def make_malbey3():
    return enemy.Enemy("Malbey Guard", 160, w.auto_shotgun, 1)
def make_malbey4():
    return enemy.Enemy("Malbey Synth", 200, w.robo_punch, 1)

toreed_list = [make_toreed1, make_toreed2, make_toreed3, make_toreed4, make_toreed5, make_toreed6, make_toreed7]
halidon_rebels = [make_halireb1, make_halireb2, make_halireb3, make_halireb4]
malbey = [make_malbey1, make_malbey2, make_malbey3, make_malbey4]

t3_list = ["toreed, halidon, malbey"]

def enemy_retrieve(etype):
    if etype == "toreed":
        return random.choice(toreed_list)
    if etype == "halidon":
        return random.choice(halidon_rebels)
    if etype == "malbey":
        return random.choice(malbey)

def random_list():
    return random.choice(t3_list)