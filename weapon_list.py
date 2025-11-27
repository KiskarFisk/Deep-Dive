import weapon_function as w
import random

# TIER I

machete = w.Weapon("Machete", 60, "A standard issue HALIDON machete, commonly found on clones.")
axe = w.Weapon("Axe", 90, "A standard axe, used commonly by firemen.")
pipe = w.Weapon("Lead Pipe", 20, "A lead pipe, nothing more nothing less.")
knife = w.Weapon("Knife", 40, "A standard knife.")
sledge = w.Weapon("Sledgehammer", 50, "A large hammer.")
# Robot shit
robo_punch = w.Weapon("Punch", 80, "")
# Special
acid = w.Weapon("Acid Vial", 100, "A vial of acid.")
# Guns
pistol = w.Weapon("Pistol", 110, "A pistol.")
auto_pistol = w.Weapon("Auto-Pistol", 120, "An Old Age auto-pistol.")

bolt_rifle = w.Weapon("Bolt Action Rifle", 130, "An old bolt action rifle, very outdated now.")
rifle = w.Weapon("Small Auto-Rifle", 150, "A New Age auto-rifle made for easy use, fairly weak because of that.")

single_shotgun = w.Weapon("Single Shot Shotgun", 150, "A shotgun with no ammo reserve and a single barrel.")
auto_shotgun = w.Weapon("Auto-Shotgun", 190, "An automatic shotgun, very effective.")
double_shotgun = w.Weapon("Double Barrel Shotgun", 160, "A shotgun with two barrels.")
triple_shotgun = w.Weapon("Triple Barrel Shotgun", 240, "A shotgun with three barrels.")
quadruple_shotgun = w.Weapon("Quad Barrel Shotgun", 360, "A shotgun with four barrels.")
five_shotgun = w.Weapon("Five Barrel Shotgun", 470, "What the hell are they doing at this point?")

dart_gun = w.Weapon("Dart Gun", 80, "A gun, that shoots darts.")
# High Tech Bable
mk0_laz_pistol = w.Weapon("Mk0 Lazer Pistol", 110, "An extremely old lazer pistol with a massive battery, its classified as a rifle because of its size.")
mk0_laz_rifle = w.Weapon("Mk0 Lazer Rifle", 130, "An old lazer rifle, the battery pack sits on your back, weighing almost 50 pounds.")
mk1_laz_pistol = w.Weapon("Mk1 Lazer Pistol", 140, "An improved version of the original lazer pistol, now properly classified as a pistol.")
mk1_laz_rifle = w.Weapon("Mk1 Lazer Rifle", 160, "The standard issue lazer rifle for nearly 40 years, now very outdated but still effective.")

t1_shop_list = [
    machete,
    axe,

    pistol,

    mk0_laz_pistol
]

t2_shop_list = [
    axe,
    pistol,
    auto_pistol,
    bolt_rifle,
    mk0_laz_pistol,
    mk0_laz_rifle
]