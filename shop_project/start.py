import tkinter as tk                    
from tkinter import ttk
  
root = tk.Tk()
root.title("Shop Demo")
root.geometry("500x500")
tabControl = ttk.Notebook(root)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Motherboard')
tabControl.add(tab2, text ='CPU')
tabControl.place(x=10,y=100)
  
mbLabel = ttk.Label(tab1, text ="Pick Motherboard")
mbLabel.grid(column = 0,row = 0, padx = 10,  pady = 10)  


mbOptions = [
    "Intel",
    "AMD"
]

def mb_changed(self, *args):
    print (mbSelected.get())

mbSelected = tk.StringVar()
mbSelected.set( "Intel" )
mbSelected.trace('w', mb_changed)
  

mbDrop = tk.OptionMenu( tab1, mbSelected, *mbOptions )
mbDrop.grid(column = 1,row = 0, padx = 10,  pady = 10)
  
#now try to add a dropdown for the cpu's on tab2

  
root.mainloop()  