import tkinter as tk
from PIL import ImageTk,Image

burgerCost = 1.10
total = 0

#main window
root = tk.Tk()
root.title("My Burger Counter")
root.geometry("400x200")
root.iconbitmap('burger.ico')
root.configure(background='PaleGreen1')
root.resizable(False,False)

#buy button
def myfunction():
    global total
    total += burgerCost
    message = "Total: £" + f'{total:.2f}' #this requires python 3.6 or higher, f-strings
    textField.config(text = message)

buyButton = tk.Button(root,text="Buy Burger",
bg="springGreen2",fg="snow", borderwidth=0,activebackground="spring green",
activeforeground="snow",font=("Arial", 20),command=myfunction)
buyButton.place(relx=0.1,rely=0.2,relwidth=0.4,relheight=0.2)

#label
textField = tk.Label(root, text="Total: £0.00",font=("Arial", 16))
textField.place(relx=0.1,rely=0.6,relwidth=0.4,relheight=0.2)

burgerImg = ImageTk.PhotoImage(file="burger.jpg")
burgerLable = tk.Label(root, image=burgerImg)
burgerLable.place(relx=0.6,rely=0.2,relwidth=0.3, relheight=0.6)


root.mainloop()



