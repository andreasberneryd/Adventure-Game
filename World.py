import random
from Level import Level

place_names = ["forest", "house", "lake", "desert", "cave"]
place_modifiers = ["an old", "a haunted", "a dark", "an uninteresting"]

item_names = ["Sword", "Axe", "Bow and Arrows"]
item_modifiers = ["Rusty", "Enchanted"]

world = []

def generate_world(world):
	sizex = 3
	sizey = 3
	
	for i in range(sizey):
		rowx = []
		generate_row(rowx, sizex)
		world.append(rowx)

def generate_row(row, size):
	for i in range(size):
		name = place_modifiers[random.randint(0,3)] + " " + place_names[random.randint(0,4)]
		row.append(Level(i, "Fascinating description", name))
