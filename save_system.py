import pickle as pkl
from player_function import player1

def save():
    with open("save_data.pkl", "wb") as f:
        pkl.dump((
            player1.serial_num,
            player1.objective,
            player1.hp,
            player1.max_hp,
            player1.rep,
            player1.credits,
            player1.energy,
            player1.energy_max,
            player1.augments,
            player1.max_augments,
            player1.last_shop,
            player1.mis_comp,
            player1.shop_inv,
            player1.tier,
            player1.weapon
            ),
        f
        )

def load():
    with open("save_data.pkl", "rb") as f:
        (
            player1.serial_num,
            player1.objective,
            player1.hp,
            player1.max_hp,
            player1.rep,
            player1.credits,
            player1.energy,
            player1.energy_max,
            player1.augments,
            player1.max_augments,
            player1.last_shop,
            player1.mis_comp,
            player1.shop_inv,
            player1.tier,
            player1.weapon
        ) = pkl.load(f)