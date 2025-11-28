import mission_function as miss
from player_function import player1
import objectives.story_objectives as sobj

# TIER 1 MISSIONS
story1 = miss.Mission("Planet-Fall on Terra", "story", 1, 3, "rat")
story2 = miss.Mission("Clear Landing Area", "story", 1, 4, "rat")
story3 = miss.Mission("Recover Weapon Shipment", "story", 1, 2, "rat")
story4 = miss.Mission("Destroy Rat Encampment", "story", 1, 4, "rat")
story5 = miss.Mission("Recover Data Banks from Old Lab", "story", 1, 3, "tienne")
story6 = miss.Mission("Raid Tienne Bunker", "story", 1, 3, "tienne")
story7 = miss.Mission("Enter Old Tokyo", "story", 1, 5, "orfast")
story8 = miss.Mission("Recover Stolen Documents in Refugee Camp", "story", 1, 4, "orfast")
story9 = miss.Mission("Hijack Plane to Leece", "story", 1, 2, "tienne")

story_miss = [story1, story2, story3, story4, story5, story6, story7, story8, story9]

def get_mission():
    return story_miss[player1.current_mission]

def get_objective():
    if player1.current_mission == 2:
        player1.objective = sobj.story2
    else:
        player1.objective = None