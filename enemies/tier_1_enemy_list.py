import enemy_function as enemy
import weapon_list as w

def make_rat_scavenger():
    return enemy.Enemy("Rat Scavenger", 170, w.machete, 1)
def make_rat_rager():
    return enemy.Enemy("Rat Berzerker", 120, w.axe, 1)
def make_rat_crackpot():
    return enemy.Enemy("Rat Crackpot", 80, w.pipe, 2)

tier1_enemy_list = [make_rat_scavenger, make_rat_rager, make_rat_crackpot]