import objective_function as obj

scav1 = obj.Objective("Scavenge Old Equipment", 3, "scavenge",
                           "A HALIDON tech team needs some materials to be scavenged from some local sites.", 10, 40)
scav2 = obj.Objective("Scavenge Old Documents", 4, "scavenge", "The HALIDON research team in Ikari needs old documents dug up.", 10, 40)

infilobj1 = obj.Objective("Wipe Out Enemy Activity", 3, "infiltrate", "Some local groups have been giving the company trouble, wipe them out.", 11, 40)

retreobj1 = obj.Objective("Retrieve Stolen Documents", 2, "retrieve",
                          "A HALIDON tech group had their documents stolen by some local gangs, track them down and return them.", 13, 40)

starter_objectives = [scav1, scav2, infilobj1, retreobj1]