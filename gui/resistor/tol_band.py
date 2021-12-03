import tkinter as tk


class Tol_band:
    option_list = [
    "brown",
    "red",
    "green",
    "blue",
    "violet",
    "grey",
    "gold",
    "silver"
    ] 

    value_list = [
        "1%",
        "2%",
        "0.5%",
        "0.25%",
        "0.1%",
        "0.05%",
        "5%",
        "10%"
    ]


    

    def __init__(self,y,root):
        self.variable = tk.StringVar(root)
        self.variable.set(self.option_list[6])
    
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
        
    def get_value(self) -> str:
        index = self.option_list.index(self.variable.get())
        return self.value_list[index]