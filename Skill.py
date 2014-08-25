class Skill:
    id = 0
    name = ""
    damage = 0

    def __init__(self, id, name, damage):
        self.id = id
        self.name = name
        self.damage = damage

    def __repr__(self):
        return self.name