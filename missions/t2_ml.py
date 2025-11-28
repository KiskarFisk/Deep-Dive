import mission_function as miss

infil1 = miss.Mission("Infiltrate Old Factory", "infiltrate", 2, 4, None)
infil2 = miss.Mission("Infiltrate Enemy Base", "infiltrate", 2, 3, None)
infil3 = miss.Mission("Infiltrate Old Research Lab", "infiltrate", 2, 2, None)

recov1 = miss.Mission("Retrieval from Old Factory", "mat_rec", 2, 4, None)
recov2 = miss.Mission("Retrieval from Old Warehouse", "mat_rec", 2, 3, None)

recov1_1 = miss.Mission("Retrieval from Old Lab", "dat_rec", 2, 3, None)
recov1_2 = miss.Mission("Retrieval from Old Data Center", "dat_rec", 2, 2, None)

t2_misslist = [infil1, infil2, infil3, recov1, recov2, recov1_1, recov1_2]