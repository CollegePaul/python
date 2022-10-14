import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

# Create two frames in the window
page_1 = tk.Frame(root, background="pink")
page_2 = tk.Frame(root, background="yellow")

#Functions for switching pages
def change_to_pink():
   page_1.place(x=150,y=0, width=350, height=400)
   page_2.place_forget()

def change_to_yellow():
   page_2.place(x=150,y=0, width=350, height=400)
   page_1.place_forget()


#page 1 stuff - pink
label1 = tk.Label(page_1, text="This is on Pink")
label1.place(x=10,y=10)

btn3 = tk.Button(page_1, text="New stuff")
btn3.place(x=10,y = 60)


#page2 stuff - yellow
label2 = tk.Label(page_2, text="This is on Yellow page")
label2.place(x=10,y = 10)

imp = tk.Entry(page_2)
imp.place(x=10,y = 60)

#These buttons are on the main form
# Add a button to switch between two frames
btn1 = tk.Button(root, text="Switch to pink page", command=change_to_pink)
btn1.place(x=10,y=10)

btn2 = tk.Button(root, text="Switch to Yellow page", command=change_to_yellow)
btn2.place(x=10,y = 60)

#the main loop
root.mainloop()