from random import randint
from random import choice
from Level import Level
from Creature import *
from Bandage import *
from Weapon import *

place_names = ["forest", "house", "lake", "desert", "cave", "ravine", "village", "beach", "river"]
place_modifiers = ["old", "haunted", "dark", "uninteresting", "dirty", "burnt"]

item_names = ["sword", "axe", "bow with arrows", "AK-47", "purple dildo"]
item_modifiers = ["a rusty", "an enchanted", "a heavy", "a dirty", "a huge"]

monster_names = ["troll", "witch"]
monster_modifiers = ["terrifying", "ugly"]

place_decriptions = ["The {0} is suspiciously {1}. You wonder what might have caused this, and the possible reasons you think of make you uneasy.",\
                     "As you arrive, a small girl calls for your attention:\n\'The {0} ahead is all {1}! Some say that terrible monsters are terrorizing these lands. You should not continue!\'\nYou consider her advise, but continue anyway.",\
                     "Not very much seems to be happening at the {1} {0}, but you know that there are plenty of dangers out there.",
                     " ",\
                     ]

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
		choice(choice(world)).creatures.append(Creature(0, name, randint(25,100), randint(5,45)))

	for i in range(0, sizey*sizex):
		name = choice(item_modifiers) + " " + choice(item_names)
		choice(choice(world)).items.append(Weapon(0, name, randint(15,50)))

	for i in range(int(sizex*sizey/2)):
		name = choice(item_modifiers) + " healing kit"
		choice(choice(world)).items.append(Bandage(0, name, randint(3,30)))

def generate_row(row, size):
	for i in range(size):
		name = choice(place_names)
		modif = choice(place_modifiers)	
		description = choice(place_decriptions).format(name, modif)
		row.append(Level(i, description, modif + " " + name))
