from tkinter import *
from tkinter import filedialog, messagebox

#make not oop
#add a menu
#add data saving and loading
#ideas - use sql to add image to database with a name for a user
#add mini preview images from database
#add paint icon

root = Tk()
root.title("PS Sprite Editor")
root.geometry("500x540")
root.configure(background = 'grey20')
root.resizable(0,0)
pi = PhotoImage(file = 'pbrush.png')
root.iconphoto(False, pi)

pen_colour = "black"
grid_colour = "#EEEEEE"
c_width = 400
c_height = 400
grid_size = 50  #400 // 8

data_labels = [] #list of the label and thier data

#make the binary data array for storing the pixels.
bin_data =[]
for rows in range(0,8): #make 8 rows of 8 and set all to zero(white)
    bin_data.append([0,0,0,0,0,0,0,0])

      
            


# save_button = Button(self.root, text = "Save", bd=4, bg='white', command=self.save_pic, width=8, relief=RIDGE)
# save_button.place(x=0,y=247)

# canvas_colour_button = Button(self.root, text = "Canvas", bd=4, bg='white', command=self.canvas_colour, width=8, relief=RIDGE)
# canvas_colour_button.place(x=0,y=277)

# make the Canvas, 1 big and a small preview canvas
canvas = Canvas(root, bg = 'white', bd=0, height=c_height, width = c_width)
canvas.place(x=20,y=20)

#canvas_small = Canvas(root, bg = 'white', bd=0, height=32, width = 32)
#canvas_small.place(x=440,y=20)



# draw pixel grid on large canvas
def draw_grid():
    for i in range(0,8):
        canvas.create_line(i*grid_size,0,i*grid_size,c_height, fill= grid_colour, width = 1) #vertical
        canvas.create_line(0,i*grid_size, c_width,i*grid_size, fill= grid_colour, width = 1) #horizontal
draw_grid()

def paint(event):
    global pen_colour
    
    #check if gone out of the canvas while moving
    if event.x > c_width -1:
        return
    if event.y > c_height -1:
        return
    
    #clamp the mouse to the nearest square
    x = int((event.x)/grid_size)        
    y = int((event.y)/grid_size) 

    x1 = x * grid_size
    y1 = y * grid_size

    #draw the pixels on the canvas
    canvas.create_rectangle(x1,y1,x1+grid_size,y1+grid_size, fill=pen_colour, outline="#EEEEEE", width=1)
    #canvas_small.create_rectangle(x*4,y*4,x*4+4,y*4+4, fill=pen_colour, outline=pen_colour, width=1)

    #set the pixel in the bin_data
    if pen_colour == "black":
        bin_data[y][x] = 1  
    else:
        bin_data[y][x] = 0

    #calculate the row total
    binary_string = ""
    for col in range(0,8):
        binary_string += str(bin_data[y][col])

    decimal = int( binary_string , 2) #convert base 2 into decimal int

    data_labels[y][1] = decimal #set the decimal value into the label

    #update the label
    data_labels[y][0].config(text=data_labels[y][1])


def erase(event):
    global pen_colour
    pen_colour = "white"
    paint(event)


    
def draw_pen(event):
    global pen_colour
    pen_colour = "black"
    paint(event)

#button to clear the canvas
def clear():
    #this will need to clear data too.
    canvas.delete('all')
    draw_grid()

    #clear the data
    global bin_data
    bin_data =[]
    for rows in range(0,8): #make 8 rows of 8 and set all to zero(white)
        bin_data.append([0,0,0,0,0,0,0,0])
    
        #calculate the row total
        binary_string = ""
        for col in range(0,8):
            binary_string += str(bin_data[rows][col])

        decimal = int( binary_string , 2) #convert base 2 into decimal int

        data_labels[rows][1] = decimal #set the decimal value into the label

        #update the label
        data_labels[rows][0].config(text=data_labels[rows][1])



clear_button = Button(root, text = "Clear", bg='white', command=clear, width=8, relief=RIDGE)
clear_button.place(x=20,y=450)
    

def save_pic():
    try:
        #filename = filedialog.asksaveasfilename(defaultextension='.txt')

        with open("test.txt", 'a') as f:
            f.truncate(0)
            global data_labels
            
            for row in data_labels:
                f.write(str(row[1]) + "\n")


        #messagebox.showinfo("Image saved as " + "text.txt")
        messagebox.showinfo("Saved", "Image saved as " + "text.txt")

    except:
        messagebox.showerror("Unable to save image, something has gone wrong")

save_button = Button(root, text = "Save", bg='white', command=save_pic, width=8, relief=RIDGE)
save_button.place(x=100,y=450)

# Mouse events
canvas.bind("<B1-Motion>", draw_pen)
canvas.bind("<B3-Motion>", erase)
canvas.bind("<Button-1>", draw_pen)
canvas.bind("<Button-3>", erase)


#make the lables for the data
for l in range(0,8):
    label = Label(root, text="0", font=('Ariel', 18, 'bold'), bg="grey20", fg = "white")
    label.place(x=440, y=l*grid_size+30)
    data_labels.append([label,0]) #add the label to a list so it can be changed later

root.mainloop()