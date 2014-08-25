from Item import Item
from random import random
from random import randint
from random import uniform
__author__ = 'andberne'

class Level:
    id = 0
    content = ""
    name = ""
    items = []
    creatures = []

    def __init__(self, id, content, name):
        self.id = id
        self.content = content
        self.name = name

    def arrive(self, player):
        print self.name
        print(self.content)
        if len(self.creatures) > 0:
            self.fight(player)

    def fight(self, player):
        creature = self.creatures[0]
        print "You just started a fight with %s!" % creature
        while creature.health > 0 and player.health > 0:
            print "Creature health: %d, Your health: %d" % (self.creatures[0].health, player.health)

            #player attack
            print player.inventory[0]
            for i in xrange(0, len(player.inventory)):
                print "%d : %s" % (i, player.inventory[i])
            weapon = int(raw_input("Pick item to attack with"))

            # for i in xrange(0, len(player.skills)):
            #     print "%d : %s" % (i, player.skills[i])
            # skill = int(raw_input("Pick skill to use"))
            #
            # player_damage = player.inventory[weapon].damage * player.skills[skill].damage * random.uniform(0.0, 1.0)
            #
            # print "You attacked monster with %s, using skill %s and dealt %d damage" % (player.inventory[i],player.skills[i])
            #
            #
            # # creature attack
            # creature_damage = randint(0, 10)
            # player.health -= creature_damage
            # print "creature attacked you and dealt %s damage" % creature_damage
