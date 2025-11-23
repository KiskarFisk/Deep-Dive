import enemy_function as enemy
import weapon_list as w

def make_rat_scavenger():
    return enemy.Enemy("Rat Scavenger", 170, w.machete)

tier1_enemy_list = [make_rat_scavenger]
