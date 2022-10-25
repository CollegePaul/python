import tkinter as tk


root = tk.Tk()
root.geometry("500x500")

# Create two frames in the window
frame1 = tk.Frame(root,bg="yellow")
frame2 = tk.Frame(root, bg="green")

# Define a function for switching the frames
def show_frame1():
   frame1.place(x =100, y =0, width=400, height=500)
   frame2.place_forget()

def show_frame2():
   frame2.place(x=100, y =0, width=400, height=500)
   frame1.place_forget()



#add things to frame 1
f1_label= tk.Label(frame1, text="This is frame 1")
f1_label.place(x = 20, y=50)


#add things to frame 2
f2_label= tk.Label(frame2, text="I am in frame 2")
f2_label.place(x = 200, y=100)


# Add a button to switch between two frames
btn1 = tk.Button(root, text="Show frame 1",  command=show_frame1)
btn1.place(x=10,y=5)

btn2 = tk.Button(root, text="Show frame 2",  command=show_frame2)
btn2.place(x=10,y=40)

root.mainloop()