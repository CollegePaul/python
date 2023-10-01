import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.resizable(False,False)
root.title("My Tkinter app")
root.config(background="green")


mylabel = tk.Label(root, text = "Hello World", font=("Ariel", 20), background="green", fg= "white")
mylabel.place(x = 10, y = 10)

def myCommand():
    day = textBox.get("1.0","end-1c")
    mylabel.config(text = day)


myButton = tk.Button(root, text = "Press Me", font=("Ariel", 20), command = myCommand, background="lightgreen")
myButton.place(x = 10, y = 50)

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

selected = tk.StringVar()
selected.set( "Monday" )
dropdown = tk.OptionMenu( root , selected, *options)
dropdown.place(x = 10, y = 150)

def picked():
    selection = "You selected the option " + str(ticked.get())
    mylabel.config(text = selection)

ticked = tk.IntVar()
r1 = tk.Radiobutton(root, text="Option 1", variable=ticked, value=1, command=picked)
r2 = tk.Radiobutton(root, text="Option 2", variable=ticked, value=2, command=picked)
r3 = tk.Radiobutton(root, text="Option 3", variable=ticked, value=3, command=picked)
r1.place(x = 400, y = 10)
r2.place(x = 400, y = 40)
r3.place(x = 400, y = 70)


CheckVar = tk.IntVar()
checkBox = tk.Checkbutton(root, text = "Tick Me", variable = CheckVar, onvalue = 1, offvalue = 0)
checkBox.place (x=10, y= 450)

textBox = tk.Text(root, width = 20, height=3)
textBox.place(x= 300, y = 300)

spinner = tk.Spinbox(root, from_=0, to=10)
spinner.place(x= 300, y = 200 )

slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
slider.place(x = 10, y = 250)


def donothing():
    print("I don't do anything, but I could...")

#make the menubar
menubar = tk.Menu(root)

#add options the file menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
#add the file menu to the menu
menubar.add_cascade(label="File", menu=filemenu)

#make the edit menu
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
#add the edit menu to the menubar
menubar.add_cascade(label="Edit", menu=editmenu)

#make the  help menu
helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
#add the help menu to the menubar
menubar.add_cascade(label="Help", menu=helpmenu)

#add the menubar to the root window
root.config(menu=menubar)


root.mainloop()