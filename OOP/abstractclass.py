from abc import ABC, abstractmethod
 
class shape(ABC):
 
    def __init__(self, colour):
        self.colour = colour
        super().__init__()
    
    @abstractmethod
    def calculateArea(self):
        pass
    
#you cant make an instance of shape as it has abstracts methods
#myShape = shape("red")

class square(shape):
    def __init__(self, colour):
        super().__init__(colour)
    
    def calculateArea(self,sideLength):
        print(sideLength*sideLength)
    

'''
The mySquare is now implimenting an instance of the concreate square class.
The calculateArea method must be implimented in the square class, it overrides the
default behaviour of this abstract method in the base class.
'''
mySquare = square("blue")
mySquare.calculateArea(4)

