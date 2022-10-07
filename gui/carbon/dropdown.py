#DROPDOWN WITH DATA
import tkinter as tk


myDictionary = {
    "heater": 4,
    "cpu": 0.5,
    "oven": 3
}

#main window
root = tk.Tk()
root.title("My Carbon calculator")
root.geometry("400x600")


root.resizable(False,False)


def doStuff():
    item = value_inside.get()
    label.config(text = myDictionary[item])

#OPTION LIST
options = ["heater", "cpu", "oven"]
value_inside = tk.StringVar(root)
value_inside.set("heater")

option_list = tk.OptionMenu(root, value_inside, *options)
option_list.place(x = 100, y = 20)
  

#BUTTON
button = tk.Button(root, text="Calculate", command= doStuff)
button.place(x=250, y=20)


#OUTPUT
label = tk.Label(root,text="")
label.place(x=100, y = 300)

root.mainloop()

