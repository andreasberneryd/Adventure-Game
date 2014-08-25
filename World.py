import random
from Level import Level

place_names = ["Forest", "House", "Lake", "Desert", "Cave"]
place_modifiers = ["Old", "Haunted", "Dark", "Uninteresting"]

item_names = ["Sword", "Axe", "Bow and Arrows"]
item_modifiers = ["Rusty", "Enchanted"]

world = []

def generate_world(world):
	sizex = 2
	sizey = 2
	
	for i in range(sizey):
		rowx = []
		generate_row(rowx, sizex)
		world.append(rowx)

def generate_row(row, size):
	for i in range(size):
		row.append(Level(i, "Fascinating description", place_names[random.randint(0,4)]))
