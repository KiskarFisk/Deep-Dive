import mission_function as miss
from player_function import player1
import objectives.story_objectives as sobj

story1 = miss.Mission("Planet-Fall on Terra", "story", 1, 3, "rat")
story2 = miss.Mission("Clear Landing Area", "story", 1, 4, "rat")

def get_mission():
    if player1.current_mission == 1:
        player1.objective = sobj.story1
        return story1
    else:
        return None

def get_objective():
    if player1.current_mission == 2:
        player1.objective = sobj.story2