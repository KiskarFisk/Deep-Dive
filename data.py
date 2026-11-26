"""All game content lives here. Add enemies, weapons, missions etc. as entries, not code."""

# (text, pause in seconds)
INTRO = [
    ("You are C{serial}.", 0.8),
    ("Welcome to the Diver program.", 1.0),
    ("Your purpose is to recover assets on behalf of the HALIDON Corporation.", 1.4),
    ("Your body has been valued at $72. Please do not waste it.", 1.1),
]

# traits: light = Heavy costs 1 less, breaker = every hit breaks guard, spread = hits all enemies
# ammo: None = melee. Ranged weapons refill at the start of each mission; empty = half damage.
WEAPONS = {
    "machete": {"name": "Machete", "dmg": 8, "price": 0, "ammo": None, "traits": [],
                "desc": "Standard issue."},
    "knife": {"name": "Knife", "dmg": 6, "price": 12, "ammo": None, "traits": ["light"], "desc": ""},
    "axe": {"name": "Fire Axe", "dmg": 11, "price": 25, "ammo": None, "traits": ["breaker"], "desc": ""},
    "pistol": {"name": "Pistol", "dmg": 12, "price": 30, "ammo": 8, "traits": [], "desc": ""},
    "shotgun": {"name": "Pipe Shotgun", "dmg": 9, "price": 40, "ammo": 4, "traits": ["spread"], "desc": ""},
}

TRAITS = {
    "light": "Heavy costs 1 less",
    "breaker": "Every hit breaks guard",
    "spread": "Hits all enemies",
}

SHOP_POOL = ["knife", "axe", "pistol", "shotgun"]

# moves cycle in order, starting at a random point. (label, kind, value)
# kinds: attack (damage), guard (halves damage taken until its next move), burn (turns of burn), idle
ENEMIES = {
    "rat_scavenger": {"name": "Rat Scavenger", "hp": 30, "loot": 3, "moves": [
        ("Slash", "attack", 7), ("Slash", "attack", 7), ("Lunge", "attack", 12)]},
    "rat_berzerker": {"name": "Rat Berzerker", "hp": 24, "loot": 3, "moves": [
        ("Swing", "attack", 8), ("Wind up", "idle", 0), ("Frenzy", "attack", 18)]},
    "rat_crackpot": {"name": "Rat Crackpot", "hp": 16, "loot": 2, "moves": [
        ("Flail", "attack", 5), ("Flail", "attack", 9)]},
    "rat_holder": {"name": "Rat Holder", "hp": 45, "loot": 4, "moves": [
        ("Brace", "guard", 0), ("Pipe", "attack", 6)]},
    "rat_acid": {"name": "Rat Acid Slinger", "hp": 18, "loot": 3, "moves": [
        ("Throw acid", "burn", 3), ("Scratch", "attack", 4), ("Scratch", "attack", 4)]},

    "tienne_scout": {"name": "Tienne Scout", "hp": 22, "loot": 4, "moves": [
        ("Knife", "attack", 6), ("Ambush", "attack", 11)]},
    "tienne_greaser": {"name": "Tienne Greaser", "hp": 26, "loot": 5, "moves": [
        ("Fire", "attack", 9), ("Take cover", "guard", 0), ("Fire", "attack", 9)]},
    "tienne_shotgunner": {"name": "Tienne Shotgunner", "hp": 28, "loot": 6, "moves": [
        ("Reload", "idle", 0), ("Blast", "attack", 20)]},
}

# Factions with an empty roster have lore only (not in the core game yet).
FACTIONS = {
    "rats": {"name": "The Rats", "roster": [
        "rat_scavenger", "rat_berzerker", "rat_crackpot", "rat_holder", "rat_acid"],
        "lore": "The Rats are a group of drug addicted scavengers, they loot and kill with glee."},
    "tienne": {"name": "Tienne", "roster": ["tienne_scout", "tienne_greaser", "tienne_shotgunner"],
        "lore": "Tienne are a group of mercenaries originating from Old Tokyo. They were once powerful "
                "enough to rival HALIDON but the company collapsed after the destruction of Japan."},
    "orfast": {"name": "Orfast", "roster": [],
        "lore": "Orfast is a group operating solely in Terran cities, they're harmless for the most part, "
                "when left alone. They fiercely fight for the so-called freedom of humanity on Terra."},
    "knights": {"name": "New Order Knights", "roster": [],
        "lore": "The New Order Knights are a group of fanatic militants. They believe themselves successors "
                "of a knightly order, which one they won't tell outsiders. Despite numerous attempts "
                "infiltration has proved impossible."},
    "toreed": {"name": "Toreed Corp.", "roster": [],
        "lore": "Toreed Corporation appeared as one of the premier mech and robotics companies. Their "
                "initial success was quickly overshadowed by HALIDON."},
    "halidon_rebels": {"name": "HALIDON Rebels", "roster": [],
        "lore": "Rebels originating from HALIDON, an utter nuisance."},
    "malbey": {"name": "Malbey", "roster": [],
        "lore": "The Malbey Company is a frontier exploration company, producing most of their equipment "
                "on Terra. Their interests do not align with those of HALIDON."},
}

MISSION_TYPES = {"salvage": "Salvage", "purge": "Purge", "recovery": "Recovery"}

MISSIONS = [
    {"name": "Strip the Kessler Foundry", "type": "salvage", "rooms": (3, 4)},
    {"name": "Sweep the Drowned Arcade", "type": "salvage", "rooms": (2, 3)},
    {"name": "Block 9 Depot Run", "type": "salvage", "rooms": (2, 4)},
    {"name": "Clear the Underpass Nest", "type": "purge", "rooms": (3, 3)},
    {"name": "Purge the Tram Yard", "type": "purge", "rooms": (2, 3)},
    {"name": "Recover the Courier Case", "type": "recovery", "rooms": (2, 3)},
    {"name": "Retake the Relay Shack", "type": "recovery", "rooms": (2, 2)},
]

OBJECTIVES = {
    "scrap_quota": {"name": "Scrap Quota", "type": "salvage", "goal": 3, "credits": 15, "rep": 40,
        "desc": "Fabrication is behind schedule. Bring back anything with a serial number."},
    "archive_request": {"name": "Archive Request", "type": "salvage", "goal": 2, "credits": 12, "rep": 40,
        "desc": "The research team in Ikari wants pre-collapse paper records. Handle with care."},
    "pest_control": {"name": "Pest Control", "type": "purge", "goal": 2, "credits": 14, "rep": 40,
        "desc": "Squatters are slowing down survey teams. Remove them."},
    "lost_property": {"name": "Lost Property", "type": "recovery", "goal": 2, "credits": 16, "rep": 40,
        "desc": "A courier went dark carrying company property. The property is what matters."},
}
