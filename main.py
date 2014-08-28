import sys
from random import choice
from Skill import Skill
from Level import Level
from Player import Player
from Input import *
from World import *
from Item import Item
from Weapon import Weapon
from Armor import Armor
from Creature import Creature
__author__ = 'andberne'

print "\nAdventure Game!\nEnter a direction (north, south, west, east) to move around or type any action (look, inventory, equip, pick up, quit)\n"

generate_world(world)
player = Player(world)

while (True):
    input = raw_input("What do you want to do? > ").lower()
    handle_input(input, player)
