from Skill import Skill


class Creature:

    id = 0
    name = ""
    health = 0
    strength = 0
    inventory = []
    skills = []

    def __init__(self, id, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength




