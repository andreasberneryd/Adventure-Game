__author__ = 'andberne'


class Creature:

    name = ""
    health = 0
    strength = 0
    inventory = []

    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength


