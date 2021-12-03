 #base class
class Building:
    def __init__(self, doors, windows):
        self.doors = doors
        self.windows = windows
    
    def set_alarm():
        print("Alarm on")

class Education(Building):
    def __init__(self, doors, windows, books):
        super().__init__(doors, windows)
        self.books = books
    def library(self):
        print("you got a book!")

class Domestic(Building):
    def __init__(self, doors, windows, cooker):
        super().__init__(doors,windows)
        self.cooker = cooker
    def cook(self):
        self.cooker.ignite()
        print("You are cooking")

class Cooker:
    def __init__(self, burners) :
        self.burners = burners
    def ignite(self):
        print("The heat is on")

aeg = Cooker(5)
my_house = Domestic(2,8,aeg)
my_house.cook()