import weapon_list as w
import enemy_function as enemy
import random

def make_tienne_scout():
    return enemy.Enemy("Tienne Scout", 110, w.knife, 1)
def make_tienne_greaser():
    return enemy.Enemy("Tienne Greaser", 110, w.pistol, 1)
def make_tienne_rifle():
    return enemy.Enemy("Tienne Rifleman", 130, w.bolt_rifle, 1)
def make_tienne_shotgun1():
    return enemy.Enemy("Tienne Shotgunner", 120, w.single_shotgun, 1)
def make_tienne_shotgun2():
    return enemy.Enemy("Tienne Shotgunner", 120, w.double_shotgun, 1)

def make_knight1():
    return enemy.Enemy("New Order Knight", 140, w.single_shotgun, 1)
def make_knight2():
    return enemy.Enemy("New Order Knight", 140, w.bolt_rifle, 1)
def make_squire():
    return enemy.Enemy("New Order Squire", 100, w.pistol, 1)

tienne_merc_list = [make_tienne_scout, make_tienne_rifle, make_tienne_greaser, make_tienne_shotgun1, make_tienne_shotgun2]
nwo_knights = [make_knight1, make_knight2, make_squire]

t2_list = ["tienne", "knight"]

def enemy_retrieve(etype):
    if etype == "tienne":
        return random.choice(tienne_merc_list)
    if etype == "knight":
        return random.choice(nwo_knights)