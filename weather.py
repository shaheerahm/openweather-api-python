from os import read
from tkinter import *
from typing import Text
import requests
import time

with open("D:\Learning and Projects\OW API - Copy\key_api.txt") as f:
             line = f.readline()

#def click():
# entered_text=cityName.get()


def getWeather(window):

    city = cityName.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + line
    json_data = requests.get(api).json()
    
    condition = json_data['weather'][0]['description'].title()
    infoCity = json_data['name']
    infoCountry = json_data['sys']['country']
    temp = int(json_data['main']['temp'])
    min_temp = int(json_data['main']['temp_min'])
    max_temp = int(json_data['main']['temp_max'])
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    visibility = json_data['visibility']
    cloud = json_data['clouds']['all']

    wind = json_data['wind']['speed']

    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    CountryData = infoCity + ", " + infoCountry

    final_info = condition + ", " + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + " °C\n" + "Min Temp: " + str(min_temp) + " °C\n" +  "Pressure: " + str(pressure)  + " hPa\n" +  "Humidity: " + str(humidity) + "%\n" +   "Visibility: " + str(visibility) + "%\n" +  "Cloudiness: " + str(cloud) + "%\n" +  "Wind Speed: " + str(wind) + " ms\n" +  "Sunrise: " + str(sunrise) + " AM\n" +  "Sunset: " + str(sunset)  + " PM"
    
    CityLabel.config(text = CountryData)
    label1.config(text = final_info)
    label2.config(text = final_data)



# window is the window
window = Tk()
window.geometry("550x500")
window.title("Weather App")
window.configure(background="black")

# font style
#f = ("Neue Helvetica", 15)
#t = ("Neue Helvetica", 35, "bold")


#Textfield for the input
cityName = Entry(window, justify='center', font = ("Neue Helvetica", 35, "bold"), bg="grey", fg="white")
cityName.pack(pady = 20)
cityName.focus()
cityName.bind('<Return>', getWeather)

#tk.Button(window, text="SUBMIT", width=6, command=click)


# City info
CityLabel = Label(window, font = ("Neue Helvetica", 25), bg="black", fg="white", justify="left")
CityLabel.pack()

# Label1 shows the weather centigrade
label1 = Label(window, font = ("Neue Helvetica", 30), bg="black", fg="white", justify="left")
label1.pack()

# Label2 shows the more Weather info
label2 = Label(window, font = ("Neue Helvetica", 15), bg="black", fg="white", justify="left")
label2.pack()

#main loop
window.mainloop()

