import tkinter as tk

class GUI:
    def __init__(self, master):
        self.master = master #this is the root object
        master.title("Example OOP") #name of root window

        #add a label
        self.label = tk.Label(master, text="Add a label" )
        self.label.place(x = 100, y=50)

        #add a button
        self.button = tk.Button(master, text="Run a function (hi)", command=self.hi)
        self.button.place(x = 200, y=200, width=120, height = 30)

        self.languages = ('Python', 'JavaScript', 'Java',
                        'Swift', 'GoLang', 'C#', 'C++', 'Scala')

        self.option_var = tk.StringVar("Pick a language")

        self.list = tk.OptionMenu(master, self.option_var,self.languages)

    def hi(self):
        print("Hello!")


#make sure this is the main program running
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('700x400')
    my_gui = GUI(root)
    root.mainloop()