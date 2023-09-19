import tkinter as tk 


root = tk.Tk()
root.geometry("500x500")

#make a canvas
canvas = tk.Canvas(root,width=400, height=400, background="blue")
canvas.place(x=50, y=50)
x1=0
x2=100
y1=0
y2=100
line1 = canvas.create_line(50, 50, 100, 100, fill="white", width=2)


def move_left(event):
    x = -2
    y = 0
    canvas.move(line1,x,y)

root.bind("<Left>", move_left)

root.mainloop() 