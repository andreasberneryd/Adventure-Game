import sys
from Level import Level
from Player import Player
from Input import *
from Item import Item
from Creature import Creature
__author__ = 'andberne'


world = [[Level(1, "first", "name1"), Level(2, "second", "name2")],\
         [Level(3, "third", "name3"), Level(4, "fourth", "name4")]]
world[0][0].items.append(Item("Sword"))
#world[0][0].creatures.append(Creature("Monster1", 100, 100))
len(world)
x = 0
y = 0

player = Player(world)
print("Enter a direction to move or type quit to quit")

def h_input(input):
	global player
	handle_input(input, player)

while (True):
    input = raw_input("What do you want to do? > ")
    h_input(input)
