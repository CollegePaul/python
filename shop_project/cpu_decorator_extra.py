class Computer:
  '''
    Abstract Class: Computer
  '''
  def __init__(self):
    if self.__class__ == Computer:
      raise NotImplementedError('Cannot create object of class Computer')
    self._description = 'Unknown Computer'
    self._make = "Unknown Make"
  
  def getDescription(self):
    return self._description

  def getMake(self):
    return self._make
  
  def cost(self):
    pass



class Intel_Computer(Computer):
  def __init__(self):
    Computer.__init__(self)
    self._description = 'An Base Intel Computer'
    self._make = "Intel"
    
  def cost(self):
    return 150

class AMD_Computer(Computer):
  def __init__(self):
    Computer.__init__(self)
    self._description = 'An Base AMD Computer'
    
  def cost(self):
    return 140


  
class Part_adder(Computer):
  def __init__(self):
    if self.__class__ == Part_adder:
      raise NotImplementedError('Cannot create object of class Part_adder')
  
  def getDescription(self):
    pass
  
class Motherboard(Part_adder):
  def __init__(self, Computer, model):
        Part_adder.__init__(self)
        self.__Computer = Computer
        self._make = self.__Computer._make
        self.model = model
   
    
  def getDescription(self):
    return self.__Computer.getDescription() + ', Motherboard:' + (self.model)
  
  def cost(self):
    return 100 + self.__Computer.cost()


class CPU(Part_adder):
  def __init__(self, Computer):
    Part_adder.__init__(self)
    self.__Computer = Computer
    
  def getDescription(self):
    return self.__Computer.getDescription() + ', CPU'
  
  def cost(self):
    return 250 + self.__Computer.cost()

class RAM(Part_adder):
  def __init__(self, Computer, amount):
    Part_adder.__init__(self)
    self.__Computer = Computer
    self._make = self.__Computer._make
    self.amount = amount
    
  def getDescription(self):
    return self.__Computer.getDescription() + ', RAM:' + str(self.amount) + " gb"
  
  def cost(self):
    return 90 + self.__Computer.cost()

  def getMake(self):
    return self._make
  

  
if __name__ == '__main__':

    myComputer = Intel_Computer()

  
    myComputer = Motherboard(myComputer, "Z760")

    myComputer = RAM(myComputer, 32)

    print (myComputer.getDescription() + ' £' + str(myComputer.cost()))
    
