from tkinter import *
from tkinter import colorchooser,filedialog, messagebox

#make not oop
#add a menu
#add data saving and loading
#ideas - use sql to add image to database with a name for a user
#add mini preview images from database
#add paint icon

root = Tk()
root.title("PS Paint")
root.geometry("800x540")
root.configure(background = 'grey')
root.resizable(0,0)

pen_colour = "black"
      
            
# clear_button = Button(self.root, text = "Clear", bg='white', command=lambda :self.canvas.delete("all"), width=8, relief=RIDGE)
# clear_button.place(x=0,y=217)

# save_button = Button(self.root, text = "Save", bd=4, bg='white', command=self.save_pic, width=8, relief=RIDGE)
# save_button.place(x=0,y=247)

# canvas_colour_button = Button(self.root, text = "Canvas", bd=4, bg='white', command=self.canvas_colour, width=8, relief=RIDGE)
# canvas_colour_button.place(x=0,y=277)

# Canvas
canvas = Canvas(root, bg = 'white', bd=0, height=400, width = 400)
canvas.place(x=80,y=20)

canvas_small = Canvas(root, bg = 'white', bd=0, height=32, width = 32)
canvas_small.place(x=660,y=0)



# draw pixel grid
for i in range(0,8):
    canvas.create_line(i*50,0,i*50,400, fill= "#EEEEEE", width = 1) #vertical
    canvas.create_line(0,i*50, 400,i*50, fill= "#EEEEEE", width = 1) #horizontal

def paint(event):
    #need to check if gone out of the canvas while moving
    if event.x > 399:
        return
    if event.y > 399:
        return
    x = int((event.x)/50) 
        
    y = int((event.y)/50) 
    x1 = x * 50
    y1 = y * 50
        
    canvas.create_rectangle(x1,y1,x1+50,y1+50, fill=pen_colour, outline="#EEEEEE", width=1)
    canvas_small.create_rectangle(x*4,y*4,x*4+4,y*4+4, fill=pen_colour, outline=pen_colour, width=1)

def erase(event):
    pen_colour = "white"
    paint(event)
    
def draw_pen(event):
    pen_colour = "black"
    paint(event)
    

def save_pic():
    try:
        filename = filedialog.asksaveasfilename(defaultextension='.jpg')
        x = root.winfo_rootx() + canvas.winfo_x() + 8
        y = root.winfo_rooty() + canvas.winfo_y() + 8
        x1 = x + canvas.winfo_width()  - 16
        y1 = y + canvas.winfo_height() - 16

        #ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
        messagebox.showinfo("Image saved as " + str(filename))

    except:
        messagebox.showerror("Unable to save image, something has gone wrong")


# Mouse events
canvas.bind("<B1-Motion>", draw_pen)
canvas.bind("<B3-Motion>", erase)
canvas.bind("<Button-1>", draw_pen)
canvas.bind("<Button-3>", erase)

root.mainloop()