import tkinter as tk


class App(tk.Tk):
  def __init__(self):
    super().__init__()

    # configure the root window
    self.title('Amazing App')
    self.geometry('400x500')

    # add a label to self.
    self.label = tk.Label(self, text='I am a label')
    self.label.place(x=160, y= 50)

    # add a button to self.
    self.button = tk.Button(self, text='I am a button', command = self.pressed)
    self.button.place(x=10, y = 90)


  def pressed(self):
    print("Pressed button")

if __name__ == "__main__":
  app = App()
  app.mainloop()