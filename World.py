from random import randint
from random import choice
from Level import Level
from Creature import *
from Weapon import *

place_names = ["forest", "house", "lake", "desert", "cave", "ravine", "village"]
place_modifiers = ["old", "haunted", "dark", "uninteresting", "dirty", "burnt"]

item_names = ["sword", "axe", "bow with arrows", "AK-47"]
item_modifiers = ["a rusty", "an enchanted", "a heavy"]

monster_names = ["troll", "witch"]
monster_modifiers = ["a terrifying", "an ugly"]

place_decriptions = ["The {0} is suspiciously {1}. You wonder what might have caused this, and the possible reasons you think of make you uneasy."]

world = []

def generate_world(world):
	sizex = 4
	sizey = 4
	
	for i in range(sizey):
		rowx = []
		generate_row(rowx, sizex)
		world.append(rowx)

	for i in range(0, int(sizex*sizey/2)):
		name = choice(monster_modifiers) + " " + choice(monster_names)
		choice(choice(world)).creatures.append(Creature(0, name, randint(25,100), randint(25,100)))

	for i in range(0, sizey*sizex):
		name = choice(item_modifiers) + " " + choice(item_names)
		choice(choice(world)).items.append(Weapon(0, name, randint(15,50)))

def generate_row(row, size):
	for i in range(size):
		name = choice(place_names)
		modif = choice(place_modifiers)	
		description = choice(place_decriptions).format(name, modif)
		row.append(Level(i, description, modif + " " + name))
