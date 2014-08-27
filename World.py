from random import randint
from Level import Level
from Creature import *
from Weapon import *

place_names = ["forest", "house", "lake", "desert", "cave"]
place_modifiers = ["an old", "a haunted", "a dark", "an uninteresting"]

item_names = ["Sword", "Axe", "Bow and Arrows"]
item_modifiers = ["Rusty", "Enchanted"]

monster_names = ["troll", "witch"]
monster_modifiers = ["terrifying", "an ugly"]

world = []

def generate_world(world):
	sizex = 4
	sizey = 4
	
	for i in range(sizey):
		rowx = []
		generate_row(rowx, sizex)
		world.append(rowx)

	for i in range(0, int(sizex*sizey/2)):
		name = monster_modifiers[randint(0,1)] + " " + monster_names[randint(0,1)]
		world[randint(0,sizey-1)][randint(0,sizex-1)].creatures.append(Creature(0, name, randint(25,100), randint(25,100)))

	for i in range(0, sizey):
		name = item_modifiers[randint(0,1)] + " " + item_names[randint(0,2)]
		world[randint(0,sizey-1)][randint(0,sizex-1)].items.append(Weapon(0, name, randint(15,50)))

def generate_row(row, size):
	for i in range(size):
		name = place_modifiers[randint(0,3)] + " " + place_names[randint(0,4)]
		row.append(Level(i, "Fascinating description", name))
