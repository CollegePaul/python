from abc import ABC, abstractmethod


class BaseComputer(ABC):
    __brand = "basic"
    __hdd = []
    __cpu = None
    __cost = 70
    __RAM = None

    """abstract base class"""
    def __init__(self):
        pass

    @abstractmethod    
    def info(self):
        return "Base Class only"

    @abstractmethod   
    def addCPU(self, cpu):
        pass

    def getSelf_brand(self):
        return self.__brand()

    def build(self):
        pass


class Intel_Computer(BaseComputer):


    """Concreate Class"""
    def __init__(self):
        self.__brand = "INTEL"
        print("INTEL made")
    def info(self):
        return "INTEL"

    def addCPU(self, cpu):
        if cpu.get_brand() == self.__brand:
            self.cpu = cpu
            return [True,""]
        else:
            return [False, "This cpu cannot be added", self.__brand, cpu.get_brand()]

    


class Amd_Computer(BaseComputer):
    """abstract base class"""
    def __init__(self):
        self.__brand = "AMD"
        pass
    def info(self):
        return "ATX"

    def addCPU(self, cpu):
        if cpu.get_brand() == self.__brand:
            self.cpu = cpu
            return [True,""]
        else:
            return [False, "This cpu cannot be added", self.__brand, cpu.get_brand()]



class CPU:
    def __init__(self, brand, name, cost) -> None:
        self.brand = brand
        self.name = name
        self.cost = cost
    
    def get_brand(self):
        return self.brand

class RAM:
    def __init__(self, size) -> None:
        self.size = size

class HDD:
    def __init__(self, size) -> None:
        self.size = size

class GPU:
    def __init__(self, card) -> None:
        self.card = card

intel = Intel_Computer()
print(intel.info())

cpu = CPU("INTEL","i7", 400)
print(intel.addCPU(cpu))
