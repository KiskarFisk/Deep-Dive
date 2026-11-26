"""Run: py test_game.py"""
import data
from combat import hit_damage

W = data.WEAPONS
assert hit_damage(W["machete"], False, 0, False) == 8
assert hit_damage(W["machete"], True, 0, False) == 20      # heavy x2.5
assert hit_damage(W["machete"], False, 0, True) == 4       # guard halves
assert hit_damage(W["machete"], True, 0, True) == 20       # heavy ignores guard
assert hit_damage(W["axe"], False, 0, True) == 11          # breaker ignores guard
assert hit_damage(W["pistol"], False, 3, False) == 12
assert hit_damage(W["pistol"], False, 0, False) == 6       # out of ammo halves

# content integrity
for f in data.FACTIONS.values():
    assert all(e in data.ENEMIES for e in f["roster"])
for w in W.values():
    assert all(t in data.TRAITS for t in w["traits"])
assert all(w in W for w in data.SHOP_POOL)
assert all(m["type"] in data.MISSION_TYPES for m in data.MISSIONS)
assert all(o["type"] in data.MISSION_TYPES for o in data.OBJECTIVES.values())
print("ok")
