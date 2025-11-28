import mission_function as miss

rat_land1 = miss.Mission("Scavenge in Abandoned Factory", "scavenge", 1, 3, None)
rat_land2 = miss.Mission("Scavenge in Abandoned Office", "scavenge", 1, 4, None)
rat_land3 = miss.Mission("Scavenge in Abandoned Warehouse", "scavenge", 1, 2, None)

infil1 = miss.Mission("Infiltrate Old Bunker", "infiltrate", 1, 3, None)
infil2 = miss.Mission("Infiltrate Base in the Slums", "infiltrate", 1, 2, None)

retrieve1 = miss.Mission("Retrieve Stolen Materials", "retrieve", 1, 3, None)
retrieve2 = miss.Mission("Intercept Stolen Materials", "retrieve", 1, 2, None)

t1_missions = [rat_land1, rat_land2, rat_land3, infil1, infil2, retrieve1, retrieve2]