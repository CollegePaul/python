import tkinter as tk  #Load the tkinter library (module)


#make a main window
root = tk.Tk()                          #root will be the name of the window
root.title("My first programme")
root.geometry("600x400")                #Size in pixels
root.configure(background='Green')       #Background Colour
root.resizable(False,False)              #Can't resize window

#button function
def myfunction():
    #This function will change the text of
    myText.config(text = "World")

#Make a button
myButton = tk.Button(root,text="Press Me",font=("Arial", 20),command=myfunction)
myButton.place(relx=0.2,rely=0.2,relwidth=0.6,relheight=0.2)

#label
myText = tk.Label(root, text="Hello",font=("Arial", 20))
myText.place(relx=0.2,rely=0.6,relwidth=0.6,relheight=0.2)

#The main loop to keep processing user events
root.mainloop()

