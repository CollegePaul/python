#TKinter Module
import tkinter as tk



#main window
root = tk.Tk()
root.title("My App")
root.geometry("400x400")
root.resizable(False,False)

#Applience
textField = tk.Label(root, text="Applience",font=("Arial", 14))
textField.place(x= 10, y = 10)
applience_entry = tk.Entry(root,font=("Arial", 14) )
applience_entry.place(x =130,y = 10)

#power
textField2 = tk.Label(root, text="Power (KW)",font=("Arial", 14))
textField2.place(x= 10, y = 50)
power_entry = tk.Entry(root,font=("Arial", 14) )
power_entry.place(x =130,y = 50)

#hours
textField3 = tk.Label(root, text="Hours",font=("Arial", 14))
textField3.place(x= 10, y = 90)
power_hours = tk.Entry(root,font=("Arial", 14) )
power_hours.place(x =130,y = 90)

#total
textField4 = tk.Label(root, text="TOTAL COST: ",font=("Arial", 14))
textField4.place(x= 10, y = 350)


def press():
    kwh = float(power_entry.get())
    hours = float(power_hours.get())
    total = (kwh * hours * 365) * 0.52
    print(kwh)
    print(hours)
    print(kwh * hours)
    [print(kwh * hours * 365)]
    textField4.config(text = "TOTAL COST: " + str(total))

#button
myButton = tk.Button(root,text="Calculate", command = press, font=("Arial", 16))
myButton.place(x= 10, y = 300)



#main loop
root.mainloop()


