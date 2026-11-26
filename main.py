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


def current_act(p):
    return data.STORY[min(p["story"], len(data.STORY) - 1)][0]


def dive(p):
    options = []  # (label, faction, rooms, is_story)
    if p["story"] < len(data.STORY):
        m = data.STORY[p["story"]][1]
        options.append((f"[bold cyan]STORY: {m['name']}[/]", m["faction"], m["rooms"], True))
        console.print(f"[dim]{m['brief']}[/]")
    if p["story"] >= 1:  # side contracts unlock after the first report
        for s in random.sample(current_act(p)["side"], 2):
            options.append((s["name"], random.choice(s["factions"]), random.randint(*s["rooms"]), False))
    for i, (label, *_) in enumerate(options, 1):
        console.print(f"{i}. {label}")
    c = Prompt.ask("Choice (0 to cancel)", choices=[str(i) for i in range(len(options) + 1)],
                   show_choices=False)
    if c == "0":
        return
    _, faction, rooms, is_story = options[int(c) - 1]
    if run_mission(p, faction, rooms):
        p["missions_done"] += 1
        if is_story:
            report(p)


def report(p):
    act, m = data.STORY[p["story"]]
    r = m["report"]
    console.rule("[bold]After-Action Report[/]")
    for speaker, text in r["lines"]:
        name = f"[bold green]C{p['serial']}[/]" if speaker == "C" else f"[bold red]{speaker}[/]"
        console.print(f"{name}: {text.format(serial=p['serial'])}")
        time.sleep(1.2)
    if r.get("credits"):
        p["credits"] += r["credits"]
        console.print(f"+{r['credits']} credits.")
    if r.get("weapon"):
        w = data.WEAPONS[r["weapon"]]
        if Prompt.ask(f"Take the {w['name']}? It replaces your {data.WEAPONS[p['weapon']]['name']}.",
                      choices=["y", "n"]) == "y":
            p["weapon"] = r["weapon"]
    p["story"] += 1
    if r.get("end_act"):
        console.rule(f"[bold]End of {act['name']}[/]")
        if p["story"] >= len(data.STORY):
            console.print("[dim]The story continues in a future update. Side contracts remain available.[/]")
    Prompt.ask("Press enter", default="", show_default=False)


def run_mission(p, faction, rooms):
    """Returns True if the mission was completed (not evacuated, not dead)."""
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
            return False
        loot += room_loot
        console.print(f"\nRoom clear. HP {p['hp']}/{p['max_hp']}. Carrying [yellow]{loot}[/] credits of salvage.")
        if room < rooms:
            if Prompt.ask("1. Push deeper  2. Evacuate", choices=["1", "2"], show_choices=False) == "2":
                p["credits"] += loot
                console.print("Evacuated. Salvage banked; mission marked failed.")
                return False

    p["credits"] += loot
    console.print(f"[green]Mission complete.[/] {loot} credits banked.")
    return True


def status(p):
    w = data.WEAPONS[p["weapon"]]
    credits = f"[red]{p['credits']} (debt)[/]" if p["credits"] < 0 else str(p["credits"])
    traits = ", ".join(data.TRAITS[t] for t in w["traits"])
    console.print(f"\n[bold]C{p['serial']}[/]  HP {p['hp']}/{p['max_hp']}  Credits {credits}")
    console.print(f"Weapon: {w['name']} ({w['dmg']} dmg{', ' + traits if traits else ''})"
                  + (f" [dim]{w['desc']}[/]" if w["desc"] else ""))
    if p["story"] < len(data.STORY):
        act, m = data.STORY[p["story"]]
        console.print(f"{act['name']}. Next: [bold cyan]{m['name']}[/] [dim]{m['brief']}[/]")
    else:
        console.print("Story complete for now.")


def main():
    p = save.load()
    if not (p and Prompt.ask(f"Resume as C{p['serial']}?", choices=["y", "n"]) == "y"):
        p = save.new_player()
        intro(p)
    while True:
        save.save(p)  # autosave every return to the menu
        console.print(f"\n[bold]C{p['serial']}[/], select an action.")
        console.print("1. Dive  2. Status  3. HALIDON Mobile Computer  0. Quit")
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
