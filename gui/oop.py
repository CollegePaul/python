import tkinter as tk

#main window
root = tk.Tk()
root.title("My list")
root.geometry("400x500")
root.configure(background='Green')

counter = 0

def addText():
    global counter
    counter += 1
    text = entry.get()
    print(text)
    textArea.insert(tk.END, str(counter) + ": " + text + "\n")
    
    

#text
textArea = tk.Text(root,height=10, width=30)
textArea.place(x=70,y=200)

#input
entry = tk.Entry(root)
entry.place(x=20, y=20, width = 200)

#button
submit = tk.Button(root, text="Add to list", command= addText)
submit.place(x=20, y=50, width = 200)


#main loop
root.mainloop()
