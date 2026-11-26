"""Deep-Dive. Run: py main.py"""
import random
import time

from rich.console import Console
from rich.prompt import Prompt

import combat
import data
import hub
import save

console = Console()


def intro(p):
    for line, pause in data.INTRO:
        console.print(line.format(serial=p["serial"]))
        time.sleep(pause)


def group_size():
    n = 1
    if random.random() < 0.4:
        n = 2
        if random.random() < 0.15:
            n = 3
    return n


def dive(p):
    options = random.sample(data.MISSIONS, 3)
    for i, m in enumerate(options, 1):
        console.print(f"{i}. {m['name']} [dim]({data.MISSION_TYPES[m['type']]})[/]")
    c = Prompt.ask("Choice (0 to cancel)", choices=["1", "2", "3", "0"], show_choices=False)
    if c == "0":
        return
    m = options[int(c) - 1]
    faction = random.choice([f for f, v in data.FACTIONS.items() if v["roster"]])
    rooms = random.randint(*m["rooms"])
    p["ammo"] = data.WEAPONS[p["weapon"]]["ammo"] or 0
    loot = 0
    console.print(f"Intel reports [bold]{data.FACTIONS[faction]['name']}[/] activity. {rooms} rooms.")

    for room in range(1, rooms + 1):
        console.rule(f"Room {room}/{rooms}")
        enemies = [combat.spawn(random.choice(data.FACTIONS[faction]["roster"])) for _ in range(group_size())]
        room_loot = sum(e["loot"] for e in enemies)
        if not combat.fight(p, enemies):
            if loot:
                console.print(f"[red]{loot} credits of salvage lost.[/]")
            hub.replace_clone(p)
            return
        loot += room_loot
        console.print(f"\nRoom clear. HP {p['hp']}/{p['max_hp']}. Carrying [yellow]{loot}[/] credits of salvage.")
        if room < rooms:
            if Prompt.ask("1. Push deeper  2. Evacuate", choices=["1", "2"], show_choices=False) == "2":
                p["credits"] += loot
                console.print("Evacuated. Salvage banked; mission marked failed.")
                return

    p["credits"] += loot
    p["missions_done"] += 1
    console.print(f"[green]Mission complete.[/] {loot} credits banked.")
    o = p["objective"]
    if o:
        obj = data.OBJECTIVES[o["id"]]
        if obj["type"] == m["type"] and o["progress"] < obj["goal"]:
            o["progress"] += 1
            console.print(f"Objective progress: {o['progress']}/{obj['goal']}.")
            if o["progress"] == obj["goal"]:
                console.print("Objective complete. Report to the Mission Center.")


def status(p):
    w = data.WEAPONS[p["weapon"]]
    credits = f"[red]{p['credits']} (debt)[/]" if p["credits"] < 0 else str(p["credits"])
    traits = ", ".join(data.TRAITS[t] for t in w["traits"])
    console.print(f"\n[bold]C{p['serial']}[/]  HP {p['hp']}/{p['max_hp']}  Credits {credits}  Rep {p['rep']}")
    console.print(f"Weapon: {w['name']} ({w['dmg']} dmg{', ' + traits if traits else ''})"
                  + (f" [dim]{w['desc']}[/]" if w["desc"] else ""))
    o = p["objective"]
    if o:
        obj = data.OBJECTIVES[o["id"]]
        console.print(f"Objective: [bold]{obj['name']}[/] {o['progress']}/{obj['goal']} "
                      f"{data.MISSION_TYPES[obj['type']]} missions. [dim]{obj['desc']}[/]")
    else:
        console.print("Objective: none. Request one at the Mission Center.")


def main():
    p = save.load()
    if not (p and Prompt.ask(f"Resume as C{p['serial']}?", choices=["y", "n"]) == "y"):
        p = save.new_player()
        intro(p)
    while True:
        save.save(p)  # autosave every return to the menu
        console.print(f"\n[bold]C{p['serial']}[/], select an action.")
        console.print("1. Dive  2. Status  3. Mission Center  0. Quit")
        c = Prompt.ask("Choice", choices=["1", "2", "3", "0"], show_choices=False)
        if c == "1":
            dive(p)
        elif c == "2":
            status(p)
        elif c == "3":
            hub.menu(p)
        else:
            console.print("Progress saved.")
            return


if __name__ == "__main__":
    main()
