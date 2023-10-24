import tkinter as tk


#setup window
master = tk.Tk()
master.geometry("600x600")
master.config(background="grey")
canvas_width = 500
canvas_height = 500

def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#cccccc")

   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#cccccc")


canvas_main = tk.Canvas(master, 
           width=canvas_width,
           height=canvas_height,borderwidth=2)
canvas_main.place(x = 50, y = 50)

checkered(canvas_main,50)

def get_rgb(rgb):
    #return "#%02x%02x%02x" % rgb  
    return f'#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}'

#use this to clam the rgb values
def clamp(number, smallest, largest):
    return max(smallest, min(number, largest))

def plot_bars(values):
    for p in range(0, len(values)):
       grey = (values[p]/400) * 255
       grey = int(grey)
       canvas_main.create_rectangle(p*50, 500-values[p],(p*50)+50,500,fill=get_rgb((grey, grey, grey)))





#draw lines
points = [20, 100, 250, 70, 100, 160, 200, 400, 340, 40]
# for p in range(0, 10):
#     canvas_main.create_line(p*50, 500-points[p], (p+1)*50, 500-points[p+1], fill="red", width=3 )

plot_bars(points)

master.mainloop()