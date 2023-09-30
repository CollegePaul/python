from tkinter import *
from tkinter import messagebox
import tracemalloc 


tracemalloc.start() #used for testing for memory leaks

#set up main window
root = Tk()
root.title("PS Sprite Editor")
root.geometry("500x540")
root.configure(background = 'grey20')
root.resizable(0,0)
pi = PhotoImage(file = 'pbrush.png')
root.iconphoto(False, pi)

#global program variables
pen_colour = "black"
grid_colour = "#EEEEEE"
canvas_size = 400
c_width = canvas_size
c_height = canvas_size
grid_size = canvas_size//8 

data_labels = [] #list of the label and thier data, tkinter label and int value

#make the binary data array for storing the pixels.
bin_data =[]
for rows in range(0,8): #make 8 rows of 8 and set all to zero(white)
    bin_data.append([0,0,0,0,0,0,0,0])


# make the Canvas
canvas = Canvas(root, bg = 'white', height=c_height, width = c_width)
canvas.place(x=20,y=20)

#make the pixel grid - this is used to 
#grid_data =[]


def draw_grid():
    for i in range(0,8):
        canvas.create_line(i*grid_size,0,i*grid_size,c_height, fill= grid_colour, width = 1) #vertical
        canvas.create_line(0,i*grid_size, c_width,i*grid_size, fill= grid_colour, width = 1) #horizontal
draw_grid()


#Draw the pixels on the canvas
#this works by deleting all the content and redrawing it all.
def paint(event):
    
   
    #check if gone out of the canvas while moving
    if event.x > c_width -1:
        return
    if event.y > c_height -1:
        return
    
    global pen_colour
    canvas.delete('all') #clear the canvas content(and memory)
    
    #clamp the mouse to the nearest square
    x = int((event.x)/grid_size)        
    y = int((event.y)/grid_size) 
    x1 = x * grid_size
    y1 = y * grid_size

    #global grid_data
      

    #set the pixel in the bin_data
    if pen_colour == "black":
        bin_data[y][x] = 1  
    else:
        bin_data[y][x] = 0

    #draw each pixel from the bin_data
    for row in range(0,8):
        for col in range(0,8):
            if bin_data[row][col] == 1:
                pen_colour = "black"
            else:
                pen_colour = "white"
            x1 = col * grid_size
            y1 = row * grid_size
            pixel = canvas.create_rectangle(x1,y1,x1+grid_size,y1+grid_size, fill=pen_colour, outline="#EEEEEE", width=1)       
    
    #calculate the row totals 
    #generate a binary string from the bin_data rows, by concatinating each column
    binary_string = ""
    for col in range(0,8):
        binary_string += str(bin_data[y][col])

    #calculate the decimal by using the built in base 2 conversion
    decimal = int( binary_string , 2) 

    #set the label to store the decimal value  [lable, value]
    data_labels[y][1] = decimal 

    #update the label
    #look into the posibity that this may also be memory inefficiant
    data_labels[y][0].config(text=data_labels[y][1])

    #when the canvas and data are updated show memory use.
    print(tracemalloc.get_tracemalloc_memory(), "bytes")


#erase the square by setting the colour to white and redrawing all grid
def erase(event):
    global pen_colour
    pen_colour = "white"
    paint(event)


#left mouse, draw a black square, redraw all   
def draw_pen(event):
    global pen_colour
    pen_colour = "black"
    paint(event)

#button to clear the canvas
def clear():
    canvas.delete('all') #delete all canvas objects
    draw_grid() #show the grid
   
    #clear the strore binary data
    global bin_data
    bin_data =[] #clear
    for rows in range(0,8): #this could be in a function and reused...
        bin_data.append([0,0,0,0,0,0,0,0])
    
        #calculate the row total
        binary_string = ""
        for col in range(0,8):
            binary_string += str(bin_data[rows][col])

        decimal = int( binary_string , 2) #convert base 2 into decimal int

        data_labels[rows][1] = decimal #set the decimal value into the label

        #update the labels
        data_labels[rows][0].config(text=data_labels[rows][1])


#buttons ------------------------
clear_button = Button(root, text = "Clear", bg='white', command=clear, width=8, relief=RIDGE)
clear_button.place(x=20,y=450)

save_text = Text(root, width=25, height=1)
save_text.place(x = 180, y= 450)


def save_pic():
    tracemalloc.stop()
    global save_text
    filename = save_text.get("1.0",END)
    
    try:
        #filename = filedialog.asksaveasfilename(defaultextension='.txt')
        with open("test.txt", 'a') as f:
            f.truncate(0)
            global data_labels
            
            for row in data_labels:
                f.write(str(row[1]) + "\n")
            
            f.write(filename)


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


#start the event loop. Nothing should be below here.
root.mainloop()