import tkinter as tk  #Load the tkinter library (module)
from tkinter import Menu

#make a main window
root = tk.Tk()                          #root will be the name of the window
root.title("My first programme")
root.geometry("400x500")                #Size in pixels
root.configure(background='Green')       #Background Colour
root.resizable(False,False)              #Can't resize window

def new():
    textArea.config(state= tk.NORMAL)
    textArea.delete("1.0", tk.END)
    
def load():
    new()
    with open("text.txt", mode='r') as f:
        text = f.read()
        textArea.insert(tk.END, text)
    

#menu
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=load)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

root.config(menu=menubar)


#text
textArea = tk.Text(root, height=10,width=30)
textArea.place(relx=0.2,rely=0.2)
textArea.insert(tk.END, "Just a text Widget\nin two lines\n")
textArea.insert(tk.END, "Just a text Widget\nin two lines\n")




root.mainloop()
