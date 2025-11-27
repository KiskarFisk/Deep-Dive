import enemy_function as enemy
import weapon_list as w
import random

def make_rat_scavenger():
    return enemy.Enemy("Rat Scavenger", 170, w.machete, 1)
def make_rat_rager():
    return enemy.Enemy("Rat Berzerker", 120, w.axe, 1)
def make_rat_crackpot():
    return enemy.Enemy("Rat Crackpot", 80, w.pipe, 2)
def make_rat_holder():
    return enemy.Enemy("Rat Holder", 240, w.pipe, 1)
def make_rat_acid():
    return enemy.Enemy("Rat Acid Slinger", 90, w.acid, 1)

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

tier1_enemy_list = [make_rat_scavenger, make_rat_rager, make_rat_crackpot, make_rat_holder, make_rat_acid]
tienne_merc_list = [make_tienne_scout, make_tienne_rifle, make_tienne_greaser, make_tienne_shotgun1, make_tienne_shotgun2]

t1_list = ["rat", "tienne"]

def enemy_retrieve(etype):
    if etype == "rat":
        return random.choice(tier1_enemy_list)
    if etype == "tienne":
        return random.choice(tienne_merc_list)


def random_list_t1():
    return random.choice(t1_list)
