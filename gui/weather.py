import tkinter as tk
import requests
from PIL import Image, ImageTk


'''
pip install requests
https://openweathermap.org/api
You postman, or output json into browser with json extension, or copy into vs code , example provided.

'''
photo = None

api_key = open("api_key.txt", "r")
key = api_key.read()

api_key.close()

def getWeather(canvas):
    city = textfield.get()
    global key
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + key
    json_data = requests.get(api).json()
    weather = json_data['weather'][0]['main']
    temperature = int(json_data['main']['temp'] - 273.15)
    min = int(json_data['main']['temp_min'] - 273.15)
    max = int(json_data['main']['temp_max'] - 273.15)
    icon = json_data['weather'][0]['icon']

    weather_icon = ImageTk.PhotoImage(file = "weatherIcons/" + icon + ".png")
    info =  weather + "\n" + str(temperature)
    final_data = "Max Temp: " + str(max) + "\n" + "Min Temp:" + str(min)

    label1.config(text = info)
    label2.config(text = final_data)
    img.config(image = weather_icon)
    img.image = weather_icon


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")


font_small= ("poppins", 15, "bold")
font_big = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = font_big)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = font_big)
label1.pack()
label2 = tk.Label(canvas, font = font_small)
label2.pack()


img_icon = ImageTk.PhotoImage(file="weatherIcons/01d.png")
img = tk.Label(canvas, image=img_icon)
img.pack()


canvas.mainloop()