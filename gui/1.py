import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Example OOP") #name of root window
        self.geometry('700x400')

        #add a label
        self.label = tk.Label(self, text="Add a label" )
        self.label.place(x = 100, y=50)

        #add a button
        self.button = tk.Button(self, text="Run a function (hi)", command=self.hi)
        self.button.place(x = 200, y=200, width=120, height = 30)

        self.languages = ('Python', 'JavaScript', 'Java',
                       'Swift', 'GoLang', 'C#', 'C++', 'Scala')

        self.option_var = tk.StringVar(self,"Pick a language")

        self.list = tk.OptionMenu(self, self.option_var,self.languages)
        self.list.place(x= 30,y=200)

    def hi(self):
        print("Hello!")


#make sure this is the main program running
if __name__ == "__main__":
    app = App()
    app.mainloop()