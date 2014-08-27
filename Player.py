from Point import Point
from Skill import Skill
from Weapon import Weapon
from Armor import Armor

class Player:

    position = Point(0,0)
    health = 100
    strength = 0
    inventory = []
    skills = []
    equipped = []

    def __init__(self, world):
        self.skills.append(Skill(0, "Sword Attack 1", 80 ))
        self.world = world
        self.world[0][0].arrive(self)

    def print_inventory(self):
        print self.inventory

    def pick_item(self):
        print "Choose item: "
        for i in xrange(0, len(self.world[self.position.y][self.position.x].items)):
            print "%d : %s" % (i, self.world[self.position.y][self.position.x].items[i])

        index = int(raw_input())
        self.inventory.append(self.world[self.position.y][self.position.x].items[index])
        self.world[self.position.y][self.position.x].items.pop(index)

    def equip_item(self):
        print "Following items can be equipped:"
        for item in xrange(len(self.inventory)):
            print "Weapons:"
            if isinstance(self.inventory[item], Weapon):
                print "%d : %s" % (item, self.inventory[item].name)
        for item in xrange(len(self.inventory)):
            print "Armor:"
            if isinstance(self.inventory[item], Armor):
                print "%d : %s" % (item, self.inventory[item].name)
        index = int(raw_input())
        self.equipped.append(self.inventory[index])
        print "%s equipped!" % self.inventory[index].name




    def look(self):
        print "You are in %s \n" % self.world[self.position.y][self.position.x].name
        print "The following items are available here: "
        print self.world[self.position.y][self.position.x].items
        print ""
        if(self.exists(-1,0)):
            print "To the north is %s" % self.world[self.position.y - 1][self.position.x].name
        if(self.exists(1,0)):
            print "To the south is %s" % self.world[self.position.y + 1][self.position.x].name
        if(self.exists(0,1)):
            print "To the east is %s" % self.world[self.position.y][self.position.x + 1].name
        if(self.exists(0,-1)):
            print "To the west is %s" % self.world[self.position.y][self.position.x - 1].name

    def exists(self, y, x):
        if len(self.world) > self.position.y+y and len(self.world[0]) > self.position.x + x:
            if (self.position.y+y >= 0) and (self.position.x+x >= 0):
                return True
        return False

    def move(self, y, x):

            if  self.exists(y, x) :
                self.position.y += y
                self.position.x += x

            else:
                print("You can't go there")
                return

            self.world[self.position.y][self.position.x].arrive(self)
