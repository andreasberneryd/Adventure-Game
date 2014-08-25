from Item import Item
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
        print "You just started a fight with %s!" % self.creatures[0]
        while self.creatures[0].health > 0 and player.health > 0:
            print "Creature health: %d, Your health: %d" % (self.creatures[0].health, player.health)
            raw_input(" > ")