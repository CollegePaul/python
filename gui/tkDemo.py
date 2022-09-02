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

        #graphics card list
        self.cardlist = ["card 1", "RTX card", "Slow Card", "old card", "AMD card"]
        self.card_dropdown = Options(self.cardlist,"graphics Card",
                                     self.master,self.changed_card,
                                     20,250)

        #memory list
        self.memoryList = ["1Gb", "2Gb", "4Gb", "32Gb"]
        self.memory_dropdown = Options(self.memoryList,"Choose Memory",
                                     self.master,self.changed_memory,
                                     20,350)

        #memory list
        self.memoryList2 = ["1Gb", "2Gb", "4Gb", "32Gb"]
        self.memory_dropdown2 = Options(self.memoryList2,"Choose Memory",
                                     self.master,self.changed_memory,
                                     300,350)
        
         


    def changed_card(self,*args):
        print(args[0])

    def changed_memory(self,*args):
        print(args[0])

    def hi(self):
        print("Hello!")

class Options:
    def __init__(self, myList, word, master, function, posx, posy):

        
        self.label = tk.Label(master, text=word, bg="green" )
        self.label.place(x = posx, y=posy-20)
       
        self.cards = myList
        self.card_val = tk.StringVar(master)
        self.card_val.set(word)

        self.card_menu = tk.OptionMenu(
            master,
            self.card_val,
            *self.cards,
            command= function
        )

        self.card_menu.place(x = posx, y=posy)




#make sure this is the main program running
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    my_gui = GUI(root)
    root.mainloop()