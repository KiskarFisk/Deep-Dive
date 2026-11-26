# Deep-Dive
A terminal roguelite about an expendable HALIDON clone, worth $72, working its way up one mission at a time.

## Roadmap

### Done
- [x] Core rebuild: data-driven content, JSON autosaves, `rich` terminal UI
- [x] Combat: telegraphed enemy intents, energy-cost actions, guard, weapon traits, ammo
- [x] Dives: salvage carried per room, push deeper or evacuate
- [x] Clone replacement on death (lose salvage and weapon, pay the clone fee)
- [x] Story track: ordered story missions per act, HALIDON after-action reports
- [x] Act I: Asia (9 story missions, side contracts, Rats / Tienne / Orfast)

### Next
- [ ] Play-test and balance Act I (enemy stats, prices, salvage, clone fee)
- [ ] Weapon descriptions
- [ ] Tiers and power progression across acts
- [ ] More enemy move types (ally shielding, multi-hit, debuffs)
- [ ] Augments

### Later
- [ ] Act II: Europe
- [ ] Mech upgrade
- [ ] Further acts

## Run
```
py -m pip install rich
py main.py
```
