# Example of how to use and option menu 

#TKinter Module
import tkinter as tk


items = {
    "heater": 4,
    "CPU": 0.5,
    "Oven": 3
}


#main window
root = tk.Tk()
root.title("My App")
root.geometry("400x400")
root.resizable(False,False)

#options
appliences = ["heater", "CPU", "Oven"]
variable = tk.StringVar(root)
variable.set("heater") # default value
applience_dropdown = tk.OptionMenu(root, variable, *appliences)
applience_dropdown.place ( x = 10, y=10)

#label
textField = tk.Label(root, text="Total: 0")
textField.place(x= 10, y = 200)

def press():
    value = variable.get()
    global items
    kw = items[value]
    
    textField.config(text = str(kw))

#button
myButton = tk.Button(root,text="get kw", command = press)
myButton.place(x= 10, y = 100)



#main loop
root.mainloop()

