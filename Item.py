__author__ = 'andberne'

class Item:
    name = ""
    damage = 0
    def __init__(self, name):
        self.name = name

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return self.name