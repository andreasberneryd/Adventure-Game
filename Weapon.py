__author__ = 'mihajlov'
from Item import Item

class Weapon(Item):
    damage = 0

    def __init__(self, id, name, damage):
        self.id = id
        self.name = name
        self.damage = damage
