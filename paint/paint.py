from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser,filedialog, messagebox
import PIL.ImageGrab as ImageGrab


class Paint():
    def __init__(self,root):
        self.root = root
        self.root.title("PS Paint")
        self.root.geometry("800x520")
        self.root.configure(background = 'white')
        self.root.resizable(0,0)

        self.pen_colour = "black"
        self.eraser_colour = "white"

        #add widgets to the window
        self.color_frame = LabelFrame(self.root, text="Color", font = ('arial', 15), bd=5, relief=RIDGE, bg = "white")
        self.color_frame.place(x = 0, y = 0, width = 70, height= 185)

        colors = ['#ff0000', '#ff4dd2', '#ffff33', '#000000','#0066ff','#660033','#4dff4d','#b300b3','#00ffff','#808080','#99ffcc','#009966']
        i=j=0
        for colour in colors:
            Button(self.color_frame, bg=colour, bd=2, relief=RIDGE, width=3,command=lambda col = colour:self.select_colour(col)).grid(row=i,column=j)
            i+=1
            if i == 6:
                i = 0
                j = 1

        self.eraser_button = Button(self.root, text = "Eraser", bd=4, bg='white', command=self.select_eraser, width=8, relief=RIDGE)
        self.eraser_button.place(x=0,y=187)

        self.clear_button = Button(self.root, text = "Clear", bd=4, bg='white', command=lambda :self.canvas.delete("all"), width=8, relief=RIDGE)
        self.clear_button.place(x=0,y=217)

        self.save_button = Button(self.root, text = "Save", bd=4, bg='white', command=self.save_pic, width=8, relief=RIDGE)
        self.save_button.place(x=0,y=247)

        self.canvas_colour_button = Button(self.root, text = "Canvas", bd=4, bg='white', command=self.canvas_colour, width=8, relief=RIDGE)
        self.canvas_colour_button.place(x=0,y=277)

        # scale for pen an eraser size
        self.pen_size_scale_frame = LabelFrame(self.root, text="Size", bd = 5, bg = 'white', font=('arial', 15, 'bold'),relief=RIDGE)
        self.pen_size_scale_frame.place(x=0, y=310, height=200, width=70)

        self.pen_size = Scale(self.pen_size_scale_frame, orient=VERTICAL, from_ = 50, to = 0, length = 170)
        self.pen_size.set(1)
        self.pen_size.grid(row=0, column = 1, padx = 15)

        # Canvas
        self.canvas = Canvas(self.root, bg = 'white', bd=5, relief=GROOVE, height=500, width = 700)
        self.canvas.place(x=80,y=0)

        # Mouse drag
        self.canvas.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x1, y1 = (event.x-2),(event.y-2)
        x2, y2 = (event.x+2),(event.y+2)

        self.canvas.create_oval(x1,y1,x2,y2, fill=self.pen_colour, outline=self.pen_colour, width=self.pen_size.get())

    def select_colour(self, col):
        self.pen_colour = col

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

            ImageGrab.grab().crop((x,y,x1,y1)).save(filename)
            messagebox.showinfo("Image saved as " + str(filename))

        except:
            messagebox.showerror("Unable to save image, something has gone wrong")

#main program start
if __name__ == "__main__":
    root = Tk()
    p = Paint(root)
    root.mainloop()