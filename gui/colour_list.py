import tkinter as tk


OptionList = [
"black",
"brown",
"red",
"orange"
] 

#main window
app = tk.Tk()
app.geometry('400x400')

def change(*args):
    colour = variable.get()
    opt.config( bg=colour)

variable = tk.StringVar(app)
variable.set(OptionList[0])
variable.trace("w", callback = change)
opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()
menu = opt.nametowidget(opt.cget('menu'))
for i in OptionList:
    index = menu.index(i)
    menu.entryconfigure(index, background=i)



app.mainloop()