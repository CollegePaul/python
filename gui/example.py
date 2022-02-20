import tkinter as tk
import tkinter.font as font
from tkinter import Entry, Menu
from functools import partial
import os
import platform

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
        i.place(x = 20, y = c * 33 + 50 )
        c += 1
    counter -= 1

def addItem(*args):
    global counter
    if counter > 9:
        print("limit reached")
        return
    
    
    item_font = font.Font(family='Comic Sans MS', size=12, weight='bold')
    

    #add a frame
    newFrame = tk.Frame(myFrame,background="#333333")
    newFrame.place(x=20, y=counter * 33 + 50, width = 350, height=32 )

    #text label
    text = l1.get()
    l1.delete(0,"end")
    global wordlist
    wordlist.append(text)
    l = tk.Label(newFrame, text= text,font=item_font,background="#333333", fg="white")
    l.place(x = 10, y = 0)

    #close button
    close = tk.Button(newFrame, text= "X", font=item_font, background="pink")
    close.config(command  = partial(del_button, newFrame, text))
    close.place(x = 300, y = 0)


    print("counter: " + str(counter))
    items.append(newFrame)
    counter +=1

def loadItem(i):
    global counter
    if counter > 9:
        print("limit reached")
        return
    
    
    item_font = font.Font(family='Comic Sans MS', size=12, weight='bold')
    

    #add a frame
    newFrame = tk.Frame(myFrame,background="#333333")
    newFrame.place(x=20, y=counter * 33 + 50, width = 350, height=32 )

    #text label
    text = i
    global wordlist
    wordlist.append(text)
    l = tk.Label(newFrame, text= text,font=item_font,background="#333333", fg="white")
    l.place(x = 10, y = 0)

    #close button
    close = tk.Button(newFrame, text= "X", font=item_font, background="pink")
    close.config(command  = partial(del_button, newFrame, text))
    close.place(x = 300, y = 0)


    print("counter: " + str(counter))
    items.append(newFrame)
    counter +=1



def new():
    global wordlist
    global counter
    global items

    #delete all the items in the list
    for i in items:
        i.destroy()

    wordlist = []
    items = []
    counter = 0
    
def load():
    new() #clear all
    with open("list.txt", mode='r') as f:
        new_list = f.readlines()
        
        for i in new_list:
            i.strip()
            loadItem(i)

def save():
    global wordlist
    with open("list.txt", mode='a') as f:
        #loop over all the items in the list
        #output as a list.
        f.truncate(0) #delete content
        for item in wordlist:
            item.strip()
            f.writelines(item + "\n")

def print_file():
    os.startfile("list.txt", "print")

root = tk.Tk()
root.geometry("500x600")
root.title("Shopping List")
root.config(background="#333333")

#menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=load)
filemenu.add_command(label="Save", command=save)
if platform.system() == "Windows":
    filemenu.add_separator()
    filemenu.add_command(label="Print", command=print_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

root.config(menu=menubar)

buttonFont = font.Font(family='Comic Sans MS', size=16, weight='bold') 
mainFont = font.Font(family='Comic Sans MS', size=22, weight='bold') 
#label
lab = tk.Label(root,text="Shopping List App", font=mainFont, fg="white", background="#333333")
lab.place( x=110, y = 20)

#entry box
l1 = tk.Entry(root, font = buttonFont,)
l1.place(x=50 ,y = 100)
l1.bind('<Return>', addItem)


b1 = tk.Button(root,text="Add item", font = buttonFont,command= addItem)
b1.place(x=340, y = 90)

#frame
myFrame = tk.Frame(root, background = '#333333')
myFrame.place(x=50, y=150, width = 400, height=400 )
print(platform.system())

root.mainloop()
