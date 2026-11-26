"""Turn-based combat: telegraphed enemy intents, energy, guard, weapon traits."""
import random
import time

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

import data

console = Console()

START_ENERGY, ENERGY_GAIN, ENERGY_MAX = 3, 2, 5
HEAVY_COST, HEAVY_MULT = 3, 2.5
GUARD_STEP, GUARD_MAX = 25, 75  # percent blocked per energy, cap
BURN_DMG = 3


def spawn(enemy_id):
    t = data.ENEMIES[enemy_id]
    return {"name": t["name"], "hp": t["hp"], "max_hp": t["hp"], "loot": t["loot"],
            "moves": t["moves"], "step": random.randrange(len(t["moves"])), "guard": False}


def intent(e):
    return e["moves"][e["step"] % len(e["moves"])]


def hit_damage(weapon, heavy, ammo, guarded):
    dmg = weapon["dmg"] * (HEAVY_MULT if heavy else 1)
    if weapon["ammo"] is not None and ammo <= 0:
        dmg /= 2  # out of ammo: pistol-whip
    if guarded and not (heavy or "breaker" in weapon["traits"]):
        dmg /= 2
    return int(dmg)


def bar(cur, mx, color, width=10):
    n = max(0, round(width * cur / mx))
    return f"[{color}]{'█' * n}[/][dim]{'░' * (width - n)}[/]"


def intent_text(move):
    label, kind, val = move
    return {"attack": f"[red]{label} ({val})[/]",
            "guard": f"[blue]{label} (guard)[/]",
            "burn": f"[green]{label} (burn {val})[/]",
            "idle": f"[dim]{label}[/]"}[kind]


def show(p, enemies, energy, guard, burn):
    t = Table(box=None, padding=(0, 2))
    for col in ("#", "Enemy", "HP", "Next"):
        t.add_column(col)
    for i, e in enumerate(enemies, 1):
        name = e["name"] + (" [blue](guarded)[/]" if e["guard"] else "")
        t.add_row(str(i), name, f"{bar(e['hp'], e['max_hp'], 'red')} {e['hp']}", intent_text(intent(e)))
    console.print()
    console.print(t)
    w = data.WEAPONS[p["weapon"]]
    line = (f"[bold]C{p['serial']}[/]  HP {bar(p['hp'], p['max_hp'], 'green')} {p['hp']}/{p['max_hp']}"
            f"   Energy [yellow]{'●' * energy}[/][dim]{'○' * (ENERGY_MAX - energy)}[/]")
    if w["ammo"] is not None:
        line += f"   Ammo {p['ammo']}/{w['ammo']}"
    if guard:
        line += f"   [blue]Guard {guard}%[/]"
    if burn:
        line += f"   [green]Burning ({burn})[/]"
    console.print(line)


def pick_target(enemies):
    if len(enemies) == 1:
        return enemies[0]
    c = Prompt.ask("Target", choices=[str(i) for i in range(1, len(enemies) + 1)])
    return enemies[int(c) - 1]


def fight(p, enemies):
    """Runs one room. Mutates p (hp, ammo) and empties enemies. Returns True if the player survives."""
    w = data.WEAPONS[p["weapon"]]
    heavy_cost = HEAVY_COST - ("light" in w["traits"])
    energy, burn = START_ENERGY, 0

    while True:
        guard = 0
        while enemies:  # player phase: act until End turn
            show(p, enemies, energy, guard, burn)
            console.print(f"1. Strike (1)  2. Heavy ({heavy_cost})  3. Guard +{GUARD_STEP}% (1)  4. End turn")
            c = Prompt.ask("Choice", choices=["1", "2", "3", "4"], show_choices=False)
            if c == "4":
                break
            if c == "3":
                if energy < 1 or guard >= GUARD_MAX:
                    console.print("[yellow]Can't guard more.[/]")
                    continue
                energy -= 1
                guard += GUARD_STEP
                continue
            heavy = c == "2"
            cost = heavy_cost if heavy else 1
            if energy < cost:
                console.print("[yellow]Not enough energy.[/]")
                continue
            energy -= cost
            targets = list(enemies) if "spread" in w["traits"] else [pick_target(enemies)]
            for e in targets:
                dmg = hit_damage(w, heavy, p["ammo"], e["guard"])
                if heavy or "breaker" in w["traits"]:
                    e["guard"] = False
                e["hp"] -= dmg
                console.print(f"You hit {e['name']} for [bold]{dmg}[/].")
                if e["hp"] <= 0:
                    console.print(f"[green]{e['name']} is down.[/]")
            if w["ammo"] is not None and p["ammo"] > 0:
                p["ammo"] -= 1
            enemies[:] = [e for e in enemies if e["hp"] > 0]

        if not enemies:
            return True

        console.print()
        for e in enemies:  # enemy phase
            label, kind, val = intent(e)
            e["step"] += 1
            e["guard"] = kind == "guard"
            if kind == "attack":
                dmg = val * (100 - guard) // 100
                p["hp"] -= dmg
                console.print(f"{e['name']} uses {label}: you take [red]{dmg}[/].")
            elif kind == "burn":
                burn = max(burn, val)
                console.print(f"{e['name']} uses {label}: [green]you're burning[/].")
            else:
                console.print(f"{e['name']} uses {label}.")
            time.sleep(0.5)
        if burn:
            p["hp"] -= BURN_DMG
            burn -= 1
            console.print(f"Acid burns you for [green]{BURN_DMG}[/].")
        if p["hp"] <= 0:
            return False
        energy = min(ENERGY_MAX, energy + ENERGY_GAIN)
