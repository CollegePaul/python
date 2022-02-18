import tkinter as tk
import tkinter.font as font
from tkinter import Entry, Menu
from functools import partial

wordlist = []
items = []
counter = 0
def del_button(button, text):
    print(text)

    index = items.index(button)
    bname = (items[index])
    bname.destroy()
    items.pop(index)
    buttons_update_positions()
    print("button count: " + str(len(items)))
    wordlist.pop(wordlist.index(text))

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

    #text label
    text = l1.get()
    global wordlist
    wordlist.append(text)
    l = tk.Label(newFrame, text= text)
    l.place(x = 10, y = 0)

    #close button
    close = tk.Button(newFrame, text= "X")
    close.config(command  = partial(del_button, newFrame, text))
    close.place(x = 300, y = 0)


    print("counter: " + str(counter))
    items.append(newFrame)
    counter +=1

def new():
    pass
    
def load():
    new()
    with open("list.txt", mode='r') as f:
        new_list = f.readlines()
        #add in code for creating buttons

def save():
    global wordlist
    with open("list.txt", mode='a') as f:
        #loop over all the items in the list
        #output as a list.
        f.truncate(0) #delete content
        for item in wordlist:
            f.writelines(item + "\n")


root = tk.Tk()
root.geometry("600x600")

#menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=load)
filemenu.add_command(label="Save", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

root.config(menu=menubar)

#entry button
l1 = tk.Entry(root)
l1.place(x=20,y = 20)

buttonFont = font.Font(family='Comic Sans MS', size=16, weight='bold')
b1 = tk.Button(root,text="Add item", font = buttonFont,command= addItem)
b1.place(x=300, y = 20)

#frame
myFrame = tk.Frame(root, background = 'Blue')
myFrame.place(x=50, y=150, width = 400, height=400 )


root.mainloop()
