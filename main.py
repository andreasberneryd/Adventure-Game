import sys
from Skill import Skill
from Level import Level
from Player import Player
from Input import *
from Item import Item
from Creature import Creature
__author__ = 'andberne'


world = [[Level(1, "first", "name1"), Level(2, "second", "name2")],\
         [Level(3, "third", "name3"), Level(4, "fourth", "name4")]]
world[0][0].items.append(Item("Sword", 10))
world[0][0].creatures.append(Creature(0, "Monster1", 100, 100))
world[0][0].creatures[0].skills.append(Skill(0, "Claw Attack", 8))

player = Player(world)

print("Enter a direction to move or type quit to quit")

while (True):
    global player
    input = raw_input("What do you want to do? > ")
    handle_input(input, player)
