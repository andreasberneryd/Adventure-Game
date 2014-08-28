__author__ = 'mihajlov'
from Item import Item

class Bandage(Item):
    heal = 0

    def __init__(self, id, name, heal):
        self.id = id
        self.name = name
        self.heal = heal
        self.equippable = False
        self.equipped = False

