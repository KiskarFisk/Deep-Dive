import objective_function as obj

story1 = obj.Objective("Make Planet-Fall on Terra", 1, "story", "To begin your diving career you must make planet-fall on Terra. Godspeed.", 2, 0)

story2 = obj.Objective("Clear the Landing Area", 1, "story",
                       "Your landing site is still buzzing with activity, clear the terrorists so you can set up an encampment", 2, 0)

story3 = obj.Objective("Recover Weapon Shipment", 1, "story",
                       "A weapon shipment had been stolen by a group of Rats, see about recovering it.", 2, 0)

story_obj_list = [story1, story2, story3]