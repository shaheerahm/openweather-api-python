from os import read
import tkinter as tk
import requests
import time

with open("D:\Learning and Projects\OW API\key_api.txt") as f:
             line = f.read()

def getWeather(canvas):

    
    city = textfield.get()
    
    api_ow = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + line
    json_data = requests.get(api_ow).json()
    
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'])
    min_temp = int(json_data['main']['temp_min'])
    max_temp = int(json_data['main']['temp_max'])
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + " °C" + "\n" + "min Temp: " + str(min_temp) + " °C"  + "\n" + "Pressure: " + str(pressure)  + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Wind Speed: " + str(wind) + " km/h" + "\n" + "Sunrise: " + str(sunrise) + " AM" + "\n" +  "Sunset: " + str(sunset)  + " PM"
    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()

canvas.geometry("550x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, justify='center', font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)


label1 = tk.Label(canvas, font = t)
label1.pack()

label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()

