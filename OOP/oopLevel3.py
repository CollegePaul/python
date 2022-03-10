#object oriented programming

class Person:
    def __init__(self,name,age):
        #attributes
        self.name = name
        self.age = age

    #method
    def hello(self):
        print("Hello I am " + self.name)

class Student(Person):
    def __init__(self, name, age, loan):
        super().__init__(name, age)
        self.loan = loan
    
    def loan_to_pay(self):
        print(self.loan)

    def make_payment(self, amount):
        self.loan -= amount

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    #overiding  - polymorphism - many forms
    def hello(self):
        print("Teacher says I am " + self.name)

p = Teacher("Paul", 49, "Computing")
p.hello()

s = Student("Tom", 19, 45)
s.hello()