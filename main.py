import sys
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

world[0][0].items.append(Weapon(0, "Rusty Sword", 10))

#world[0][0].creatures.append(Creature(0, "Monster1", 100, 100))
#world[0][0].creatures[0].skills.append(Skill(0, "Claw Attack", 8))

player = Player(world)

print("Enter a direction to move or type quit to quit")

while (True):
    global player
    input = raw_input("What do you want to do? > ")
    handle_input(input, player)
