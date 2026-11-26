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

    "orfast_volunteer": {"name": "Orfast Volunteer", "hp": 18, "loot": 2, "moves": [
        ("Swing", "attack", 5), ("Hold the line", "guard", 0)]},
    "orfast_militia": {"name": "Orfast Militiaman", "hp": 26, "loot": 4, "moves": [
        ("Fire", "attack", 9), ("Fire", "attack", 9), ("Take cover", "guard", 0)]},
    "orfast_rifleman": {"name": "Orfast Rifleman", "hp": 22, "loot": 5, "moves": [
        ("Take aim", "idle", 0), ("Shot", "attack", 16)]},
}

# Factions with an empty roster have lore only (not in the core game yet).
FACTIONS = {
    "rats": {"name": "The Rats", "roster": [
        "rat_scavenger", "rat_berzerker", "rat_crackpot", "rat_holder", "rat_acid"],
        "lore": "The Rats are a group of drug addicted scavengers, they loot and kill with glee."},
    "tienne": {"name": "Tienne", "roster": ["tienne_scout", "tienne_greaser", "tienne_shotgunner"],
        "lore": "Tienne are a group of mercenaries originating from Old Tokyo. They were once powerful "
                "enough to rival HALIDON but the company collapsed after the destruction of Japan."},
    "orfast": {"name": "Orfast", "roster": ["orfast_volunteer", "orfast_militia", "orfast_rifleman"],
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

# The game is railroaded: each act has story missions played in order.
# Side missions (random, for credits) unlock after the first story report.
# report lines: (speaker, text). Speaker "C" prints as the player's serial. {serial} is filled in.
# report extras: "credits" (int), "weapon" (offered, player may decline), "end_act" (prints act end).
ACTS = [
    {"name": "Act I: Asia",
     "side": [
         {"name": "Strip the Kessler Foundry", "factions": ["rats"], "rooms": (3, 4)},
         {"name": "Sweep the Drowned Arcade", "factions": ["rats", "tienne"], "rooms": (2, 3)},
         {"name": "Block 9 Depot Run", "factions": ["rats", "orfast"], "rooms": (2, 4)},
         {"name": "Clear the Underpass Nest", "factions": ["rats"], "rooms": (3, 3)},
         {"name": "Purge the Tram Yard", "factions": ["tienne", "orfast"], "rooms": (2, 3)},
         {"name": "Recover the Courier Case", "factions": ["tienne"], "rooms": (2, 3)},
         {"name": "Retake the Relay Shack", "factions": ["orfast"], "rooms": (2, 2)},
     ],
     "story": [
         {"name": "Planetfall", "faction": "rats", "rooms": 2,
          "brief": "Your drop pod is inbound for Terra. Secure the landing site and await instructions.",
          "report": {"lines": [
              ("HALIDON", "C{serial}, you are operational. That already puts you ahead of the last three units."),
              ("HALIDON", "Side contracts are now available on your Mobile Computer. Earn your keep.")]}},
         {"name": "Hold the Landing Site", "faction": "rats", "rooms": 3,
          "brief": "Hostiles are converging on the landing site. Classify them as terrorists and respond accordingly.",
          "report": {"lines": [
              ("C", "They were scavengers. Most of them weren't armed."),
              ("HALIDON", "Then they were poorly armed terrorists.")]}},
         {"name": "The Missing Crates", "faction": "rats", "rooms": 3,
          "brief": "A HALIDON weapons shipment went missing near the coast. The Rats took it. Take it back.",
          "report": {"credits": 10, "lines": [
              ("HALIDON", "Shipment recovered at 64% integrity. The shortfall has been noted on your record.")]}},
         {"name": "Burn the Nest", "faction": "rats", "rooms": 4,
          "brief": "The Rats have a camp in the old rail tunnels. HALIDON would like it to stop existing.",
          "report": {"lines": [
              ("C", "Some of them tried to surrender."),
              ("HALIDON", "Surrender is not a recognized outcome. Proceed to your next assignment.")]}},
         {"name": "The Ikari Vault", "faction": "tienne", "rooms": 3,
          "brief": "Tienne mercenaries are looting a pre-collapse lab outside Ikari. Recover its data banks before they're sold.",
          "report": {"lines": [
              ("HALIDON", "The Ikari research team thanks you."),
              ("C", "What was on the drives?"),
              ("HALIDON", "You are not cleared to know that.")]}},
         {"name": "Bunker Four", "faction": "tienne", "rooms": 3,
          "brief": "Tienne is operating out of an old defense bunker. Their contract ends today.",
          "report": {"lines": [
              ("C", "Who hired them?"),
              ("HALIDON", "Irrelevant.")]}},
         {"name": "Into Old Tokyo", "faction": "orfast", "rooms": 4,
          "brief": "HALIDON is expanding into the Old Tokyo ruins. Local militia are resisting. Clear a path.",
          "report": {"weapon": "pistol", "lines": [
              ("HALIDON", "Field performance acceptable."),
              ("HALIDON", "You are authorized to keep a recovered sidearm.")]}},
         {"name": "Camp Records", "faction": "orfast", "rooms": 4,
          "brief": "Stolen HALIDON documents are being held in a refugee camp in the ruins. Retrieve them. Collateral is pre-approved.",
          "report": {"lines": [
              ("C", "These are census records. Names of everyone in the camp."),
              ("HALIDON", "Correct. Thank you for retrieving them.")]}},
         {"name": "Wheels Up", "faction": "tienne", "rooms": 2,
          "brief": "Tienne keeps a cargo plane on an old airstrip at the edge of the city. HALIDON needs it, and you on it.",
          "report": {"end_act": True, "lines": [
              ("C", "Where am I going again?"),
              ("HALIDON", "Leece. It's in Europe."),
              ("C", "And what am I doing there?"),
              ("HALIDON", "Proving your worth.")]}},
     ]},
]

# Flat, ordered story track: STORY[i] = (act, mission)
STORY = [(act, m) for act in ACTS for m in act["story"]]
