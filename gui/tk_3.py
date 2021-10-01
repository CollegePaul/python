"""demo by Paul of the GUI"""

import tkinter as tk  #Load the tkinter library (module)

id = 0

#I did not impliment the abstract class
class Polygon():
    def sides():
        return "I have 0 sides"

class Square(Polygon):
    def sides(self):
        return "I is tri and have 3"

class Triangle(Polygon):
    def sides(self):
        return "Me square and 4"

class Pentagon(Polygon):
    def sides(self):
        return "Sir Pentagon, 5"

#instantiate the objects
square = Square()
trinagle = Triangle()
pent = Pentagon()

#add them to a list
shapes = [square,trinagle,pent]

#make a main window
root = tk.Tk()                          #root will be the name of the window
root.title("My first programme")
root.geometry("600x400")                #Size in pixels
root.configure(background='Green')       #Background Colour
root.resizable(False,False)              #Can't resize window

#button functions
def minus():
    global id #allow the function to access the id defined above
    id = id -1 
    if id < 0:   #check if the id is negative, wrap it to the end
        id = len(shapes)-1
    idText.config(text = "ID " + str(id))  #change the buttons text
    myText.config(text = shapes[id].sides())
def plus():
    global id
    id = id +1
    if id == len(shapes):
        id=0
    idText.config(text = "ID " + str(id))
    myText.config(text = shapes[id].sides())
    

#Buttons
minusButton = tk.Button(root,text="<",font=("Arial", 20),command=minus)
minusButton.place(relx=0.2,rely=0.7,relwidth=0.2,relheight=0.1)

plusButton = tk.Button(root,text=">",font=("Arial", 20),command=plus)
plusButton.place(relx=0.2,rely=0.5,relwidth=0.2,relheight=0.1)

#lables
idText = tk.Label(root, text="ID = 0",font=("Arial", 20))
idText.place(relx=0.2,rely=0.05,relwidth=0.6,relheight=0.1)

myText = tk.Label(root, text="I is tri and have 3",font=("Arial", 20))
myText.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.2)

#The main loop to keep processing user events
root.mainloop()

