"""Player state and JSON save/load."""
import json
import random
from pathlib import Path

import data

SAVE_PATH = Path(__file__).with_name("save.json")


def new_serial():
    return random.randint(100, 999999)


def new_player():
    return {
        "serial": new_serial(),
        "hp": 100, "max_hp": 100,
        "credits": 10, "rep": 0,
        "weapon": "machete", "ammo": 0,
        "objective": {"id": random.choice(list(data.OBJECTIVES)), "progress": 0},
        "missions_done": 0,
        "shop": [], "shop_at": -1,
    }


def save(p):
    SAVE_PATH.write_text(json.dumps(p, indent=2))


def load():
    if not SAVE_PATH.exists():
        return None
    p = new_player()
    p.update(json.loads(SAVE_PATH.read_text()))  # new fields get defaults on old saves
    return p
