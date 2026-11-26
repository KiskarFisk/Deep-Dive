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
for act in data.ACTS:
    assert len(act["side"]) >= 2  # dive offers 2 side missions
    for s in act["side"]:
        assert all(data.FACTIONS[f]["roster"] for f in s["factions"])
    for m in act["story"]:
        assert data.FACTIONS[m["faction"]]["roster"]
        assert m["report"].get("weapon", "machete") in W
        assert all(spk in ("C", "HALIDON") for spk, _ in m["report"]["lines"])
print("ok")
