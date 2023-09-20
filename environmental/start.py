#TKinter Module
import tkinter as tk

value = 0

#main window
root = tk.Tk()
root.title("My App")
root.geometry("400x200")
root.resizable(False,False)

#label
textField = tk.Label(root, text="Total: 0",font=("Arial", 16))
textField.place(x= 10, y = 10)

def press():
    print("Button has been pressed.")
    global value
    value = value + 1
    textField.config(text = "Total:" + str(value))

#button
myButton = tk.Button(root,text="Press Me", command = press, font=("Arial", 16))
myButton.place(x= 10, y = 60)



#main loop
root.mainloop()


