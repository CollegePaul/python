import tkinter as tk


class GUI:
    def __init__(self, master):
        self.master = master #this is the root object
        master.title("Example OOP") #name of root window

        #add a label
        self.label = tk.Label(master, text="I am a just label" )
        self.label.place(x = 100, y=50)

        #add a button
        self.button = tk.Button(master, text="Run a function (hi)", command=self.hi)
        self.button.place(x = 200, y=200)


    def hi(self):
        print("Hello!")
       

#make sure this is the main program running
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    my_gui = GUI(root)
    root.mainloop()