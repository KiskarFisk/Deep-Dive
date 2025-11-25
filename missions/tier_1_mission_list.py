import mission_function as miss
import enemies.tier_1_enemy_list as t1e

rat_land1 = miss.Mission("Scavenge in Abandoned Factory", "scavenge", 1, 3)
rat_land2 = miss.Mission("Scavenge in Abandoned Office", "scavenge", 1, 4)
rat_land3 = miss.Mission("Scavenge in Abandoned Warehouse", "scavenge", 1, 2)

t1_missions = [rat_land1, rat_land2, rat_land3]