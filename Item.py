__author__ = 'andberne'

class Item:
    name = ""
    id = 0
    equipped = False
    equippable = False

    def __init__(self, name, id):
        self.name = name

    def __repr__(self):
        return self.name
