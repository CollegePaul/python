from tkinter import *
from tkinter import colorchooser,filedialog, messagebox

#make not oop
#add a menu
#add data saving and loading
#ideas - use sql to add image to database with a name for a user
#add mini preview images from database
#add paint icon


class Paint():
    def __init__(self,root):
        self.root = root
        self.root.title("PS Paint")
        self.root.geometry("800x540")
        self.root.configure(background = 'white')
        self.root.resizable(0,0)

        self.pen_colour = "black"
      
            
        self.clear_button = Button(self.root, text = "Clear", bg='white', command=lambda :self.canvas.delete("all"), width=8, relief=RIDGE)
        self.clear_button.place(x=0,y=217)

        self.save_button = Button(self.root, text = "Save", bd=4, bg='white', command=self.save_pic, width=8, relief=RIDGE)
        self.save_button.place(x=0,y=247)

        self.canvas_colour_button = Button(self.root, text = "Canvas", bd=4, bg='white', command=self.canvas_colour, width=8, relief=RIDGE)
        self.canvas_colour_button.place(x=0,y=277)

        # Canvas
        self.canvas = Canvas(self.root, bg = 'white', bd=0, height=400, width = 400)
        self.canvas.place(x=80,y=20)

        self.canvas_small = Canvas(self.root, bg = 'white', bd=0, height=32, width = 32)
        self.canvas_small.place(x=660,y=0)

        # Mouse drag
        self.canvas.bind("<B1-Motion>", self.draw_pen)
        self.canvas.bind("<B3-Motion>", self.erase)
        self.canvas.bind("<Button-1>", self.draw_pen)
        self.canvas.bind("<Button-3>", self.erase)

        # draw pixel grid
        for i in range(0,8):
            self.canvas.create_line(i*50,0,i*50,400, fill= "#EEEEEE", width = 1) #vertical
            self.canvas.create_line(0,i*50, 400,i*50, fill= "#EEEEEE", width = 1) #horizontal

    def paint(self, event):
        #need to check if gone out of the canvas while moving
        if event.x > 399:
            return
        if event.y > 399:
            return
        x = int((event.x)/50) 
        
        y = int((event.y)/50) 
        x1 = x * 50
        y1 = y * 50
        
        self.canvas.create_rectangle(x1,y1,x1+50,y1+50, fill=self.pen_colour, outline="#EEEEEE", width=1)
        self.canvas_small.create_rectangle(x*4,y*4,x*4+4,y*4+4, fill=self.pen_colour, outline=self.pen_colour, width=1)

    def erase(self, event):
        self.pen_colour = "white"
        self.paint(event)
    
    def draw_pen(self, event):
        self.pen_colour = "black"
        self.paint(event)
        


    def select_eraser(self):
        self.pen_colour = self.eraser_colour

    def canvas_colour(self):
        colour = colorchooser.askcolor()
        #print(colour)
        self.canvas.configure(background=colour[1])
        self.eraser_colour = colour[1]

    def save_pic(self):
        try:
            filename = filedialog.asksaveasfilename(defaultextension='.jpg')
            x = self.root.winfo_rootx() + self.canvas.winfo_x() + 8
            y = self.root.winfo_rooty() + self.canvas.winfo_y() + 8
            x1 = x + self.canvas.winfo_width()  - 16
            y1 = y + self.canvas.winfo_height() - 16

            #ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            messagebox.showinfo("Image saved as " + str(filename))

        except:
            messagebox.showerror("Unable to save image, something has gone wrong")

#main program start
if __name__ == "__main__":
    root = Tk()
    p = Paint(root)
    root.mainloop()