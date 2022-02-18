import tkinter as tk
import tkinter.font as font
from functools import partial

items = []
counter = 0
def del_button(button):

    index = items.index(button)
    bname = (items[index])
    bname.destroy()
    items.pop(index)
    buttons_update_positions()
    print("button count: " + str(len(items)))

def buttons_update_positions():
    global counter
    c = 0
    for i in items:
        i.place(x = 20, y = c * 31 + 50 )
        c += 1
    counter -= 1

def addItem():
    global counter

    #add a frame
    newFrame = tk.Frame(myFrame, background = 'pink')
    newFrame.place(x=20, y=counter * 31 + 50, width = 350, height=30 )

    #text button
    button_text = l1.get()
    b = tk.Button(newFrame, text= button_text)
    #b.config(command  = partial(del_button, b ))
    print(b.cget('text'))
    b.place(x = 10, y = 0)

    #close button
    close = tk.Button(newFrame, text= "X")
    close.config(command  = partial(del_button, newFrame ))
    close.place(x = 300, y = 0)


    print("counter: " + str(counter))
    items.append(newFrame)
    counter +=1

root = tk.Tk()
root.geometry("600x600")

l1 = tk.Entry(root)
l1.place(x=20,y = 20)

buttonFont = font.Font(family='Comic Sans MS', size=16, weight='bold')
b1 = tk.Button(root,text="Add item", font = buttonFont,command= addItem)
b1.place(x=300, y = 20)

#frame
myFrame = tk.Frame(root, background = 'Blue')
myFrame.place(x=50, y=150, width = 400, height=400 )


root.mainloop()
