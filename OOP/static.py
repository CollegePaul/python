class PaulMath():
    name = "Paul"  #class attribute

    def __init__(self,age) -> None:  #instance attribute
        self.age = age

    @staticmethod   #has to be the for the instance to be able to call a static method
    def add(n1,n2):
        print(n1+n2)
        #cannot accces class attributes or instance attributes


PaulMath.add(3,4)

pm = PaulMath(49) #instance - requires the @staticmethod decorator
pm.add(2,3) 