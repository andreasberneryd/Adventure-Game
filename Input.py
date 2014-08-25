from Level import *
from Player import *
from Item import *
from Creature import *

move = ["north", "n", "south", "s", "west", "w", "east", "e"]
action = ["look", "l", "pick up", "p", "inventory", "i"]
comm = ["quit", "q"]

def handle_input(input, player):
	global move, action, comm
	if input in move:
		pass
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

def handle_movement(input, player):
	if input in move[0:2]:
		player.move()
