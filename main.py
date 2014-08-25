import sys
from Level import Level
from Player import Player
from Item import Item
from Creature import Creature
__author__ = 'andberne'


world = [[Level(1, "first", "name1"), Level(2, "second", "name2")],\
         [Level(3, "third", "name3"), Level(4, "fourth", "name4")]]
world[0][0].items.append(Item("Sword"))
world[0][0].creatures.append(Creature("Monster1", 100, 100))
len(world)
x = 0
y = 0

player = Player(world)
print("Enter a direction to move or type quit to quit")

def handle_input(input):
    global player
    if input == "north":
        player.move(-1, 0)
    elif input == "south":
        player.move(1, 0)
    elif input == "west":
        player.move(0, -1)
    elif input == "east":
        player.move(0, 1)
    elif input == "look":
        player.look()
    elif input == "pick item":
        player.pick_item()
    elif input == "inventory":
        player.print_inventory()
    elif input == "quit":
        sys.exit(0)
    else:
        print("invalid input")


while (True):
    input = raw_input("What do you want to do? > ")
    handle_input(input)
