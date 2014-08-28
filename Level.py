from Item import Item
from random import *
from random import randint
import sys
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
            #player attack
            # print player.inventory[0]
            # for i in xrange(0, len(player.inventory)):
            #     print "%d : %s" % (i, player.inventory[i])
            # weapon = int(raw_input("Pick item to attack with"))
            print player.skills[0].name
            for i in xrange(0, len(player.skills)):
                print "%d : %s" % (i, player.skills[i])

            valid_input = False
            while not valid_input:
                skill = int(raw_input("Pick skill to use: "))
                if skill < len(player.skills):
                    valid_input = True
                else:
                    print "invalid input type the number of the object to pick"

            player_damage = player.skills[skill].damage * random()
            creature.health -= player_damage
            print ""
            print "You attacked the {0} using skill {1} and dealt {2} damage".format(creature.name, player.skills[i], int(player_damage))
            print""
            if creature.health <= 0:
                print "you killed the %s" %creature.name
                break


            # creature attack
            creature_damage = int(creature.strength * random())
            player.health -= creature_damage
            print "%s attacked you and dealt %d damage" % (creature.name, creature_damage)


            if player.health <= 0:
                print "game over you died motha fucka!"
                sys.exit(0)

            roundcounter = roundcounter + 1

