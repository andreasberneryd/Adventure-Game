from Point import Point
from Skill import Skill
from Weapon import Weapon
from Armor import Armor

class Player:

    position = Point(0,0)
    health = 100
    strength = 0
    inventory = [Weapon(0, "Fist attack", 50)]
    skills = []

    def __init__(self, world):
        self.skills.append(Skill(0, "Sword Attack 1", 80 ))
        self.skills.append(Skill(0, "Sword Attack 2", 80 ))
        self.world = world
        self.world[0][0].arrive(self)

    def print_inventory(self):
        print self.inventory

    def pick_up(self):
        if len(self.world[self.position.y][self.position.x].items) > 0:
            print ""
            print "-----Pick up items-----: "
            print ""
            for i in xrange(0, len(self.world[self.position.y][self.position.x].items)):
                print "%d : %s" % (i, self.world[self.position.y][self.position.x].items[i])

            print ""
            print "%d : Take all." % (len(self.world[self.position.y][self.position.x].items))
            print "%d : Back." % (len(self.world[self.position.y][self.position.x].items) + 1)
            print ""
            index = int(raw_input("Choose >"))
            while index < 0 or index > len(self.world[self.position.y][self.position.x].items) + 1:
                index = int(raw_input("Choose >"))
            if index == len(self.world[self.position.y][self.position.x].items):
                for i in xrange(0, len(self.world[self.position.y][self.position.x].items)):
                    self.inventory.append(self.world[self.position.y][self.position.x].items[i])
                self.world[self.position.y][self.position.x].items = []
            elif index < len(self.world[self.position.y][self.position.x].items) and index >= 0:
                self.inventory.append(self.world[self.position.y][self.position.x].items[index])
                self.world[self.position.y][self.position.x].items.pop(index)
            else:
                "" #go back
        else:
            print ""
            print "[There are no items to pick up in this area.]"
            print ""

    def equip(self):
        temp = []
        print "-----Equip-----"
        print ""
        print "Your equipped items are:"
        for i in xrange(len(self.inventory)):
            if self.inventory[i].equipped == True:
                temp.append(self.inventory[i])
        if len(temp) == 0:
            print "[None.]"
        temp = []
        for i in xrange(len(self.inventory)):
            if self.inventory[i].equipped == True:
                temp.append(self.inventory[i])
                print "[%s] : %s" % (self.inventory[i].__class__.__name__, self.inventory[i].name)
        print ""
        temp = []
        print "Following items can be equipped:"
        print ""
        for i in xrange(len(self.inventory)):
            if self.inventory[i].equippable == True and self.inventory[i].equipped == False:
                temp.append(self.inventory[i])
                print "%d : %s [%s]" % (len(temp) - 1, self.inventory[i].name, self.inventory[i].__class__.__name__)
        if len(temp) > 0:
            print ""
            index = int(raw_input("Choose >"))
            while type(index) != int or index >= len(temp):
                print "Invalid input!"
                print ""
                index = int(raw_input("Choose >"))
            for i in xrange(len(self.inventory)):
                if type(self.inventory[i]) == type(temp[index]) and self.inventory[i].equipped == True:
                    self.inventory[i].equipped = False
            temp[index].equipped = True
        if len(temp) == 0:
            print "[None.]"





    def look(self):
	if len(self.world[self.position.y][self.position.x].items) == 0:
		return
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
