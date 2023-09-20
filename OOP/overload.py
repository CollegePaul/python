#operator overloading

class CoOrdinate():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str: #overloaded ther print method
        return "({},{})".format(self.x,self.y)

    def __add__(self, other): #overloaded add method
        self.x = self.x + other
        self.y = self.y + other
        return self

c = CoOrdinate(2,3)
c = c + 1
print(c)