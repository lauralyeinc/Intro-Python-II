from item import Item

class Sword(Item):
    def __init__(self, name, decription, color, strongness, powers = None):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.color = color
        self.strongness = strongness
        if powers is None:
            self.powers = []
        else:
            self.powers = powers
    
    def __str__(self):
        return f'\n This {self.name} sword is {self.color}, with the strongness of {self.strongness}, the history is: {self.description}, with the powers of: {self.powers}. '
