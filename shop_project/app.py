import computerMain
import tkinter as tk

class App:
    def __init__(self, root) -> None:
        self.message = ""
        self.root = root
        self.root.geometry("500x500")
        self.button = tk.Button(root,text = "Submit", command = self.submit)
        self.button.place(x = 100, y = 430, width = 300, height = 50)
        self.message = tk.Label(root, text = self.message)


    def submit(self):
        print("submitting")

class Dropdown:
    def __init__(self,root, options,x1,y1, label):
        self.variable = tk.StringVar(root)
        self.variable.set("Choose an option:")
        self.dropdown = tk.OptionMenu(root, self.variable, *options)
        self.dropdown.place(x = x1,y = y1 + 20,width = 300,height=40)
        self.label = tk.Label(text = label)
        self.label.place(x = x1, y = y1, width=300,height = 20)

    def get_val(self):
        return self.variable.get()





root = tk.Tk()
app = App(root)
make = Dropdown(root,["INTEL","AMD"], 50, 100,"Intel or AMD system:")
processor = Dropdown(root,["i5","i7","i9","Ryzen 3", "Ryzen 5", "Ryzen 7"], 50, 160,"Processor:")

root.mainloop()

