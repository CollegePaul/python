import tkinter as tk

class Band:
    """
    Resistor band class, a dropdown colour picker
    
    Attributes
    ----------
    option_list : list
        a list of all the colours

    Methods
    -------
    change(*args) -> none
        update the value on the button, sets colour

    get_value() -> int
        returns the index of the colour
    
    """
    option_list = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white"
    ] 

    
    def __init__(self,y,root):
        self.variable = tk.StringVar(root)
        self.variable.set(self.option_list[0])
    
        self.opt = tk.OptionMenu(root, self.variable, *self.option_list)
        self.opt.config(width=90, font=('Helvetica', 12))
        self.variable.trace("w", callback = self.change)
        self.opt.place(relx=0.0,rely=y,relwidth=1, relheight=0.1)
        menu = self.opt.nametowidget(self.opt.cget('menu'))
        for i in self.option_list:
            index = menu.index(i)
            menu.entryconfigure(index, background=i)
        self.change()


    def change(self,*args):
        colour = self.variable.get()
        self.opt.config( bg=colour)
        


    def get_value(self) -> int:
        """This function will return the index value of the colour"""
        return self.option_list.index(self.variable.get())

    