from Item import Item
from random import *
from random import randint
import sys
from Bandage import *
__author__ = 'andberne'

class Level:

    def __init__(self, id, content, name):
        self.id = id
        self.content = content
        self.name = name
	self.items = []
	self.creatures = []

    def arrive(self, player):
        print "You have arrived at the " + self.name
        print(self.content)
        if len(self.creatures) > 0:
            self.fight(player)

# returns index of picked object
    def object_picker(self, objects, message):
        print message
        for i in xrange(0, len(objects)):
            if not isinstance(objects[i], Bandage):
                print "%d : %s, damage: %d" % (i, objects[i], objects[i].damage)

        while True:
            try:
                index = int(raw_input(message))
            except:
                print "input must be a number"
                continue
            if index < len(objects):
                return index
            else:
                print "Invalid input, type the number in front of the object to pick"


    def fight(self, player):
        creature = self.creatures[0]
        roundcounter = 1
        print ""
	print "You hear something approaching, and you draw your weapons."
        print "You just started a fight with the %s!" % creature
        while True:
            print ""
            print "-----Fight Round %d-----" %roundcounter
            print ""
            print "Creature health: %d, Your health: %d" % (self.creatures[0].health, player.health)
            # Pick a weapon
            for i in xrange(0, len(player.inventory)):
                if isinstance(player.inventory[i], Bandage):
                   input = raw_input("You have bandages would you like to use them? ")
                   if(input == "yes"):
                       player.health = max(player.health + player.inventory[i].heal, 100)
                       player.inventory.pop(i)
                       print "your health is now %s" % player.health
                       break
                   else:
                       break
                    #print "%d : %s, damage: %d" % (i, objects[i], objects[i].damage)

            # Pick a skill
            weapon_index = self.object_picker(player.inventory, "Pick a weapon to use: ")

            player_damage = player.inventory[weapon_index].damage * uniform(0.7, 1.0)
            creature.health -= player_damage

            print ""
            print "You attacked the {0} using skill {1} and dealt {2} damage".format(creature.name, player.inventory[weapon_index], int(player_damage))
            print""
            if creature.health <= 0:
                print "you killed the %s" %creature.name
                self.creatures.remove(creature)
                break


            # creature attack
            creature_damage = int(creature.strength * random())
            player.health -= creature_damage
            print "%s attacked you and dealt %d damage" % (creature.name, creature_damage)


            if player.health <= 0:
                print "game over you died motha fucka!"
                sys.exit(0)

            roundcounter = roundcounter + 1

