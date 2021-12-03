
import tkinter as tk
from band import Band
from tol_band import Tol_band

output_text = "0 ohms"

 
root = tk.Tk()
root.geometry('400x400')
root.title("Resistor value app")

message = tk.Label(text = "Pick the 4 bands:" ,font=("Courier", 22))
message.place(relx=0,rely=0.1,relwidth=1,relheight=0.1)

band_1 = Band(0.2,root)
band_2 = Band(0.3,root)
band_3 = Band(0.4,root)
band_4 = Tol_band(0.5,root)


def cal_resistance(*args):
    tens = band_1.get_value() * 10
    units = band_2.get_value()
    multiplier = 10**band_3.get_value()
    output_text = (tens + units) * multiplier
    tolerance = band_4.get_value()
    output_string = str(output_text) + " ohms " + tolerance
    output.config(text = output_string)


band_1.variable.trace("w", callback = cal_resistance)
band_2.variable.trace("w", callback = cal_resistance)
band_3.variable.trace("w", callback = cal_resistance)
band_4.variable.trace("w", callback = cal_resistance)

output = tk.Label(text = output_text,font=("Courier", 22) )
cal_resistance()
output.place(relx=0,rely=0.8,relwidth=1,relheight=0.1)


root.mainloop()



