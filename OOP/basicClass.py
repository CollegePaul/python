"""
    A basic implimentation of a class part 1
"""

class Person:
    def __init__(self, name, age): #intalizer - (constructor)
        self.name = name #property , class member variable, attruibute, field
        self.age = age   #property , class member variable, attruibute, field

    def getName(self):  #method (procedure, subroutine, function)
        return self.__name


p1 = Person("Paul", 48) #object  - class instance
print(p1.name)
print(p1.age)


"""
    In the example below the name property is private and cannot be accessed directly
    We have made 'getters and setters' that allow access to these properties.
"""



# class Person:
#     """The person class is a basic human with name and age"""
#     def __init__(self, name : str, age : int) -> None:
#         self.__name = name
#         self.age = age

#     def get_name(self) -> str: 
#         """Returns string conatining the persons name"""
#         return self.__name
    
#     def set_name(self, name : str) -> None:
#         """Set the persons name, expecting a string"""
#         if type(name) == str:
#             self.__name = name
#         else:
#             print("[Error] : cannot set name")

# #you can't chane __name directly now.
# p1 = Person("Paul", 48)
# p1.set_name("Paul Smith")
# print(p1.get_name())
# print(p1.age)



#These line below will crash the program as __name is not accessable
#print(p1.__name)

#try setting the name to a number

#create the getters and setters for the age. With validation to ensure age is a number



