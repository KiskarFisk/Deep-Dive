import weapon_function as w
from player_function import player1
import random

# TIER I

machete = w.Weapon("Machete", 60, "A standard issue HALIDON machete, commonly found on clones.")
axe = w.Weapon("Axe", 90, "A standard axe, used commonly by firemen.")
pipe = w.Weapon("Lead Pipe", 20, "A lead pipe, nothing more nothing less.")
knife = w.Weapon("Knife", 40, "A standard knife.")
sledge = w.Weapon("Sledgehammer", 50, "A large hammer.")
# Special
acid = w.Weapon("Acid Vial", 100, "A vial of acid.")
# Guns
pistol = w.Weapon("Pistol", 110, "A pistol.")
bolt_rifle = w.Weapon("Bolt Action Rifle", 130, "An old bolt action rifle, very outdated now.")
single_shotgun = w.Weapon("Single Shot Shotgun", 150, "A shotgun with no ammo reserve and a single barrel.")
double_shotgun = w.Weapon("Double Barrel Shotgun", 160, "A shotgun with two barrels.")
dart_gun = w.Weapon("Dart Gun", 80, "A gun, that shoots darts.")
# High Tech Bable
mk0_laz_pistol = w.Weapon("Mk0 Lazer Pistol", 110, "An extremely old lazer pistol with a massive battery, its classified as a rifle because of its size.")

t1_shop_list = [
    machete,
    axe,

    pistol,

    mk0_laz_pistol
]
