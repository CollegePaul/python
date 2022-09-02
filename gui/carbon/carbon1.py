from colorsys import yiq_to_rgb
import tkinter as tk
from PIL import ImageTk,Image



burgerCost = 1.10
total = 0

#main window
root = tk.Tk()
root.title("My Carbon calculator")
root.geometry("400x600")
#root.iconbitmap('burger.ico')

root.resizable(False,False)


def doStuff():
    kwh = input_KWH.get()
    try:
        kwh = float(kwh)
        value = kwh * 0.233
        label.config(text=str(value)+" Kg")
        print(value, "Kg")
    except:
        print(kwh)
   



input_KWH = tk.Entry(root)
input_KWH.place(x=100,y= 20)

button = tk.Button(root, text="Calculate", command= doStuff)
button.place(x=100, y=60)


label = tk.Label(root,text="")
label.place(x=100, y = 300)

root.mainloop()

