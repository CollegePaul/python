import tkinter as tk

class band:
    Option_list = ["black","brown","red","orange"]

    def __init__(self, root):
        self.variable = tk.StringVar(root)
        self.variable.set(self.Option_list[0])
        self.variable.trace("w", callback= self.change)

        self.opt = tk.OptionMenu(root,self.variable,*self.Option_list)

        menu = self.opt.nametowidget(self.opt.cget('menu'))
        for i in self.Option_list:
            index = menu.index(i)
            menu.entryconfigure(index, background = i)

        self.opt.pack()
        
    def change(self,*args):
        colour = self.variable.get()
        self.opt.config(bg= colour )

