"""HALIDON Mission Center: objectives, armory, upgrades, medpod, faction records, cloning."""
import math
import random
import time

from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

import data
import save

console = Console()

MEDPOD_HP_PER_CREDIT = 10
HP_UPGRADE, HP_UPGRADE_COST = 20, 15
CLONE_FEE = 20


def menu(p):
    actions = {"1": turn_in, "2": new_objective, "3": armory, "4": upgrades, "5": medpod, "6": records}
    while True:
        console.print(Panel(
            "1. Turn in objective\n2. Request objective\n3. Armory\n4. Upgrades\n5. Medpod\n"
            "6. Faction records [dim](contains spoilers)[/]\n0. Leave",
            title="HALIDON Mission Center", expand=False))
        c = Prompt.ask("Choice", choices=[*actions, "0"], show_choices=False)
        if c == "0":
            return
        actions[c](p)


def turn_in(p):
    o = p["objective"]
    if not o:
        console.print("You have no objective.")
        return
    obj = data.OBJECTIVES[o["id"]]
    if o["progress"] < obj["goal"]:
        console.print(f"Objective incomplete: {o['progress']}/{obj['goal']}.")
        return
    p["credits"] += obj["credits"]
    p["rep"] += obj["rep"]
    p["objective"] = None
    console.print(f"[green]Objective complete.[/] +{obj['credits']} credits, +{obj['rep']} reputation.")


def new_objective(p):
    if p["objective"]:
        console.print("You already have an objective.")
        return
    p["objective"] = {"id": random.choice(list(data.OBJECTIVES)), "progress": 0}
    obj = data.OBJECTIVES[p["objective"]["id"]]
    console.print(f"[bold]{obj['name']}[/]: {obj['desc']}")


def armory(p):
    if p["shop_at"] != p["missions_done"]:  # stock rotates after every completed mission
        p["shop"] = random.sample(data.SHOP_POOL, 3)
        p["shop_at"] = p["missions_done"]
    t = Table(title="Armory", title_justify="left")
    for col in ("#", "Weapon", "Dmg", "Ammo", "Trait", "Price"):
        t.add_column(col)
    for i, wid in enumerate(p["shop"], 1):
        w = data.WEAPONS[wid]
        t.add_row(str(i), w["name"], str(w["dmg"]), str(w["ammo"] or "-"),
                  ", ".join(data.TRAITS[x] for x in w["traits"]) or "-", str(w["price"]))
    console.print(t)
    console.print(f"Credits: {p['credits']}. [dim]Buying replaces your current weapon.[/]")
    c = Prompt.ask("Buy (0 to leave)", choices=["1", "2", "3", "0"], show_choices=False)
    if c == "0":
        return
    wid = p["shop"][int(c) - 1]
    w = data.WEAPONS[wid]
    if wid == p["weapon"]:
        console.print("You already carry that.")
    elif p["credits"] < w["price"]:
        console.print("[red]Insufficient credits.[/]")
    else:
        p["credits"] -= w["price"]
        p["weapon"] = wid
        console.print(f"Equipped {w['name']}.")


def upgrades(p):
    console.print(f"1. +{HP_UPGRADE} max HP ({HP_UPGRADE_COST} credits)   0. Leave")
    if Prompt.ask("Choice", choices=["1", "0"], show_choices=False) == "0":
        return
    if p["credits"] < HP_UPGRADE_COST:
        console.print("[red]Insufficient credits.[/]")
        return
    p["credits"] -= HP_UPGRADE_COST
    p["max_hp"] += HP_UPGRADE
    p["hp"] += HP_UPGRADE
    console.print(f"Max HP is now {p['max_hp']}.")


def medpod(p):
    missing = p["max_hp"] - p["hp"]
    if missing <= 0:
        console.print("You're at full HP.")
        return
    max_spend = min(p["credits"], math.ceil(missing / MEDPOD_HP_PER_CREDIT))
    console.print(f"HP {p['hp']}/{p['max_hp']}. {MEDPOD_HP_PER_CREDIT} HP per credit. You have {p['credits']} credits.")
    if max_spend <= 0:
        console.print("[red]You can't afford treatment.[/]")
        return
    while True:
        n = IntPrompt.ask(f"Credits to spend (0-{max_spend})", default=max_spend)
        if 0 <= n <= max_spend:
            break
    healed = min(missing, n * MEDPOD_HP_PER_CREDIT)
    p["hp"] += healed
    p["credits"] -= n
    console.print(f"Recovered {healed} HP.")


def records(p):
    ids = list(data.FACTIONS)
    for i, fid in enumerate(ids, 1):
        console.print(f"{i}. {data.FACTIONS[fid]['name']}")
    c = Prompt.ask("Read (0 to leave)", choices=[str(i) for i in range(len(ids) + 1)], show_choices=False)
    if c != "0":
        console.print(Panel(data.FACTIONS[ids[int(c) - 1]]["lore"], expand=False))
        Prompt.ask("Press enter", default="", show_default=False)


def replace_clone(p):
    old = p["serial"]
    p.update(serial=save.new_serial(), hp=p["max_hp"], weapon="machete", credits=p["credits"] - CLONE_FEE)
    console.print(f"\n[red]Signal lost. C{old} has been written off. Asset value: $72.[/]")
    time.sleep(1.2)
    console.print("Fabricating replacement...")
    time.sleep(1.2)
    console.print(f"C{p['serial']} is now active. A clone fee of {CLONE_FEE} credits has been deducted.")
    time.sleep(1)
