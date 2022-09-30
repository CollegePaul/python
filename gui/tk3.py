import tkinter as tk


class GUI:
    def __init__(self, master):
        self.master = master #this is the root object
        master.title("Example OOP") #name of root window

        #add a label
        self.label = tk.Label(master, text="Total: " )
        self.label.place(x = 400, y=100)
        self.label.config(font=("Ariel", 16))

        #add a button
        self.button = tk.Button(master, text="Calculate",bg="green", foreground="white", command=self.hi)
        self.button.place(x = 400, y=50)
        self.button.config(font=("Ariel", 16))

        cards = ["card 1", "generic card", "slow card", "ultra card"]
        self.card_options = OptionMenu(cards,master,self.card_changed,50,50,"GPU:") #composition

        memory = ["1 gb", "4 gb", "8gb", "16 gb"]
        self.memory_options = OptionMenu(memory,master,self.card_changed,270,50,"Mem:")


    def hi(self):
        print("Hello!")

    def card_changed(self, *args):
        print(*args)

class OptionMenu():
    def __init__(self, list, master, function,posx,posy, lab):
        
        self.cards = list
        self.card_var = tk.StringVar(master)
        self.card_var.set("Default")

        self.label = tk.Label(master, text = lab)
        self.label.place(x = posx - 50, y = posy + 6)
        self.label.config(font=("Ariel", 16))

        self.card_menu = tk.OptionMenu(
            master,
            self.card_var,
            *self.cards,
            command=function)
        self.card_menu.place(x= posx,y=posy)
        self.card_menu.config(font=("Ariel", 16))


#make sure this is the main program running
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('600x400')
    my_gui = GUI(root)
    root.mainloop()