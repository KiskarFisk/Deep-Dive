import objective_function as obj

infilobj1 = obj.Objective("Wipe Out Enemy Activity", 2, "infiltrate", "Some local groups have been giving the company trouble, wipe them out.", 8, 50)
infilobj2 = obj.Objective("Wipe Out Enemy Activity", 3, "infiltrate", "Some local groups have been giving the company trouble, wipe them out.", 10, 50)

mat_rec1 = obj.Objective("Retrieve Stolen Machinery", 3, "mat_rec", "Some new machinery was stolen, recover it.", 10, 50)
mat_rec2 = obj.Objective("Retrieve Stolen Tools", 2, "mat_rec", "Some tools were stolen, recover them.", 8, 50)

dat_rec1 = obj.Objective("Recover Data", 3, "dat_rec", "Papers were stolen from a group of HALIDON researchers, recover it.", 10, 50)
dat_rec2 = obj.Objective("Obtain Documents", 2, "dat_rec", "The lab boys want some research papers uncovered, find them.", 9, 50)

t2_objs = [infilobj1, infilobj2, mat_rec1, mat_rec2, dat_rec1, dat_rec2]