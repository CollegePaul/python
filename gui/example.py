import tkinter as tk
import tkinter.font as font
from functools import partial

items = []
counter = 0
def del_button(n):
    print(n)
    bname = (items[n])
    bname.destroy()
    items.pop(n)
    buttons_update_positions()

def buttons_update_positions():
    global counter
    c = 0
    for i in items:
        i.place(x = 200, y = c * 30 + 50 )
        c += 1
    counter = len(items)-1

def addItem():
    global counter
    button_text = l1.get()
    
    b = tk.Button(myFrame, text= button_text, command  = partial(del_button, counter))
    
    b.place(x = 20, y = counter * 30 + 50)
    items.append(b)
    counter +=1

root = tk.Tk()
root.geometry("600x600")

l1 = tk.Entry(root)
l1.place(x=20,y = 20)

buttonFont = font.Font(family='Comic Sans MS', size=16, weight='bold')
b1 = tk.Button(root,text="Submit", font = buttonFont,command= addItem)
b1.place(x=300, y = 20)

#frame
myFrame = tk.Frame(root, background = 'Blue')
myFrame.place(x=50, y=150, width = 400, height=400 )


root.mainloop()
