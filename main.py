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

generate_world(world)
player = Player(world)

print("Enter a direction to move or type quit to quit")

while (True):
    input = raw_input("What do you want to do? > ").lower()
    handle_input(input, player)
