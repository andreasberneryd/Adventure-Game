__author__ = 'mihajlov'
from Item import Item

class Armor(Item):
    damage_reduction = 0

    def __init__(self, id, name, damage_reduction):
        self.id = id
        self.name = name
        self.damage_reduction = damage_reduction
