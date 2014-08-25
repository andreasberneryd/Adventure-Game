from Item import Item
from random import *
from random import randint
import sys
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

# returns index of picked object
    def object_picker(self, objects, message):
        for i in xrange(0, len(objects)):
                print "%d : %s" % (i, objects[i])

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
        print "You just started a fight with %s!" % creature
        while True:
            print "Creature health: %d, Your health: %d" % (self.creatures[0].health, player.health)
            # Pick a weapon

            # Pick a skill
            skill_index = self.object_picker(player.skills, "Pick a skill to use: ")

            player_damage = player.skills[skill_index].damage * random()
            creature.health -= player_damage

            print "You attacked %s using skill %s and dealt %d damage" % (creature, player.skills[skill_index], player_damage)

            if creature.health <= 0:
                print "you killed the monster!"
                self.creatures.remove(creature)
                break


            # creature attack
            creature_damage = int(creature.strength * random())
            player.health -= creature_damage
            print "%s attacked you and dealt %d damage" % (creature, creature_damage)


            if player.health <= 0:
                print "game over you died motha fucka!"
                sys.exit(0)

