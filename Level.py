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
        print "You have arrived at " + self.name
        print(self.content)
        if len(self.creatures) > 0:
            self.fight(player)



    def fight(self, player):
        creature = self.creatures[0]
        print "You just started a fight with %s!" % creature
        while True:
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
            print "You attacked the creature using skill %s and dealt %d damage" % (player.skills[i], player_damage)

            if creature.health <= 0:
                print "you killed the monster!"
                break


            # creature attack
            creature_damage = int(creature.strength * random())
            player.health -= creature_damage
            print "creature attacked you and dealt %s damage" % creature_damage


            if player.health <= 0:
                print "game over you died motha fucka!"
                sys.exit(0)

