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





#draw lines
points = [0 ,20, 100, 250, 70, 100, 160, 200, 400, 340, 40]
for p in range(0, 10):
    canvas_main.create_line(p*50, 500-points[p], (p+1)*50, 500-points[p+1], fill="red", width=3 )



master.mainloop()