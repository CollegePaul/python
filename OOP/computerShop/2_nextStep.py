import tkinter as tk


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Amazing App')
    self.geometry('400x500')

    # add a label to self.
    self.label = Label('I am a label', self)
    self.label = tk.Label(self, text='I am a label')
    self.label.place(x=160, y= 50)

    # add a button to self.
    self.button = tk.Button(self, text='I am a button', command = self.pressed)
    self.button.place(x=10, y = 90)


  def pressed(self):
    print("Pressed button")


class Label:
    def __init__(self,text, master, xPos, yPos, colour):
        self.label = tk.Label(text, master, backround = colour)
        self.label.place(x = xPos, y = yPos)

    def update_text(self,new_text):
        self.label.config(text=new_text)


if __name__ == "__main__":
  app = App()
  app.mainloop()