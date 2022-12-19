
from abc import ABC, abstractmethod

class Pizza(ABC):
    """abstract base class"""
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def cost(self):
        pass

class SmallPizza(Pizza):
    def __inti__(self, base):
        super.__init__(self,base)
    
    def cost(self):
        return 1.20

    def get_description(self):
        return("small pizza")


class Topping_Decorator:
    _pizza: Pizza = None  #protected attribute

    def __init__(self, pizza: Pizza) -> None:
        self._pizza = pizza  
        
    def cost(self) -> str:
        return "Decorated " + str(self._pizza.cost())

    def get_description(self):
        return self._pizza.get_description()

class Cheese(Topping_Decorator):
    def cost(self) -> str:
        return 0.10 + self._pizza.cost()

    def get_description(self):
        return self._pizza.get_description() + " Cheese"


class Ham(Topping_Decorator):
    def cost(self) -> str:
        return .20 + self._pizza.cost()

    def get_description(self):
        return self._pizza.get_description() + " Ham"

#ps = Pizza("Bread")

sp = SmallPizza("bread")

sp = Cheese(sp)

print(sp.cost())

print(sp.get_description())



# sp = Ham(sp)
# sp = Ham(sp)
# print(sp.cost())

# print(sp.get_description())
