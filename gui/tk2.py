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
        self.button.place(x = 200, y=200)


        self.cards = ["card 1", "generic card", "slow card", "ultra card"]
        self.card_var = tk.StringVar(self.master)

        self.card_menu = tk.OptionMenu(
            master,
            self.card_var,
            *self.cards,
            command=self.card_changed)
        self.card_menu.place(x= 30,y=200)


    def hi(self):
        print("Hello!")

    def card_changed(self, *args):
        print(self.card_var.get())




#make sure this is the main program running
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    my_gui = GUI(root)
    root.mainloop()