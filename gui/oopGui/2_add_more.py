import tkinter as tk


class GUI:
    def __init__(self, master):
        self.master = master #this is the root object
        master.title("Example OOP") #name of root window

        self.cpu = Entry(master,"CPU", "Submit", 10,10, self.cpu_method)  #compositon
        self.gpu = Entry(master,"GPU", "Submit", 10,60)
        self.ram= Entry(master,"RAM", "Submit", 10,110)

    def cpu_method(self):
        print("I can do CPU stuff that is special eg " + self.cpu.getEntryValue())
        



class Entry():
    def __init__(self, master, caption, buttonCaption, xPos, yPos, method= None):
        self.caption = caption
        self.label = tk.Label(master, text=caption , font=("Ariel", 16))
        self.label.place(x = xPos, y=yPos)
        self.entry = tk.Entry(master, font=("Ariel", 16))
        self.entry.place (x =xPos + 60, y = yPos, width = 100)
        self.button = tk.Button(master, text=buttonCaption, command=method or self.submit)
        self.button.place(x = xPos + 180, y=yPos)

    def submit(self):
        value = self.entry.get()
        print("you have pressed the " + value + " button")

    def getEntryValue(self):
        return self.entry.get()

       

#make sure this is the main program running
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('400x400')
    my_gui = GUI(root)
    root.mainloop()