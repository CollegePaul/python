import tkinter as tk

root = tk.Tk()
root.geometry('600x600')

def my_function():
    print("you pressed me")

my_button = tk.Button(root, text = "Press Me", command=my_function)
my_button.place(x=100, y = 50, width = 400, height = 50)

my_canvas = tk.Canvas(root, background="white")
my_canvas.place(x=100, y=150, width=400, height=300)

root.mainloop()




