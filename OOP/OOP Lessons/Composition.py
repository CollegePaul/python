#composition

class weapon():
    def __init__(self,name, cost, dmg):
        self.name = name
        self.cost = cost
        self.dmg = dmg


class armour():
    def __init__(self, name, cost) -> None:
        self.name = name
        self.cost = cost

#composition, the character is composed of(made up)
#of other classes
class character():
    def __init__(self, weapon, armour) -> None:
        self.weapon = weapon
        self.aromour = armour
        