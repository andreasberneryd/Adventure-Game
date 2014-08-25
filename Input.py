import sys
from Level import *
from Player import *
from Item import *
from Creature import *

move = ["north", "n", "south", "s", "west", "w", "east", "e"]
action = ["look", "l", "pick up", "p", "inventory", "i", "equip", "e"]
comm = ["quit", "q"]

def handle_input(input, player):
	global move, action, comm
	if input in move:
		handle_movement(input, player)
	elif input in action:
		handle_action(input, player)
	elif input in comm:
		print "Are you sure you want to quit? > "
		if raw_input() in ["yes", "y"]:
			sys.exit(0)
	else:
		print "invalid input"

def handle_action(input, player):
	if input in action[0:2]:
		player.look()
	if input in action[2:4]:
		player.pick_item()
	if input in action[4:6]:
		player.print_inventory()
	if input in action[6:8):
		player.equip()

def handle_movement(input, player):
	if input in move[0:2]:
		player.move(-1,0)
	if input in move[2:4]:
		player.move(1,0)
	if input in move[4:6]:
		player.move(0,-1)
	if input in move[6:8]:
		player.move(0,1)
