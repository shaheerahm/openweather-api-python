from os import read
from tkinter import *
import requests
import time

with open('keyapi.txt') as f:
             line = f.readline()

def click():
    try:
         entered_text = getWeather(window)
    except:
        pass

def getWeather(window):

    city = cityName.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=" + line
    json_data = requests.get(api).json()
    
    condition1 = json_data['weather'][0]['description'].title()
    infoCity1 = json_data['name']
    infoCountry1 = json_data['sys']['country']
    temp1 = int(json_data['main']['temp'])
    min_temp1 = int(json_data['main']['temp_min'])   
    max_temp1 = int(json_data['main']['temp_max'])
    pressure1 = json_data['main']['pressure']
    humidity1 = json_data['main']['humidity']
    visibility1 = json_data['visibility']
    cloud1 = json_data['clouds']['all']
    wind1 = json_data['wind']['speed']
    sunrise1 = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset1 = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 21600))

    CountryData1 = infoCity1 + ", " + infoCountry1
    infoCity.config( text = CountryData1)
    tempCurrent.config(text= condition1+ ", "+ str(temp1) +" °C")
    min_tempCurrent.config(text= str(min_temp1) + " °C")
    max_tempCurrent.config(text=str(max_temp1)+ " °C" )
    pressureCurrent.config(text= str(pressure1) + " hpa")
    humidityCurrent.config(text=str(humidity1)+ " %")
    visibilityCurrent.config(text=str(visibility1)+ " %")
    cloudCurrent.config(text=str(cloud1)+ " %")
    windCurrent.config(text=str(wind1)+ " m/s")
    sunriseCurrent.config(text=str(sunrise1)+ " AM")
    sunsetCurrent.config(text=str(sunset1)+ " PM")

# window is the window
window = Tk()
window.geometry("500x520") #se 320x568
window.title("Weather App")
window.resizable(0,0)
#window Icon
p1 = PhotoImage(file = 'icon.png')
# Setting icon of master window
window.iconphoto(False, p1)
window.configure(background="#1A1A1A")

header_top = Label(text="Weather Today", font=("Inter", 25, "bold"), fg="#4FC0B6", bg="#1A1A1A")
header_top.place(x=0,y=0,height=40,width=500)
#Textfield for the input
cityName = Entry(window, justify='center', font = ("Inter", 35, "bold"), bg="grey", fg="white")
cityName.focus()
cityName.bind('<Return>', getWeather)
cityName.place(x=0, y=40, width=400, height=40)
# Creating button
searchButton = Button(window, text = 'Search', font=("Inter",12, "bold"), fg="white", bg="#4FC0B6", command=click)
searchButton.place(x=400, y=40, width=100, height=40)


# City name Label and City name gotten from Search
#CityLabel = Label(window, text="City: ", font = ("Inter", 15, "bold"), justify='left')
#CityLabel.place(x=0,y=80,width=150, height=40)
infoCity = Label(window, font=("Inter", 30, "bold"), fg="#4FC0B6")
infoCity.place(x=0,y=80,height=40,width=500)
###############################################################################
temp = Label(window,text="Temp: ", font=("Inter", 15, "bold"), justify='left')
temp.place(x=0,y=120,height=40,width=150)
tempCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
tempCurrent.place(x=150,y=120,height=40,width=350)
###############################################################################
min_temp = Label(window,text="Min Temp: ", font=("Inter", 15, "bold"), justify='left')
min_temp.place(x=0,y=160,height=40,width=150)
min_tempCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
min_tempCurrent.place(x=150,y=160,height=40,width=350)
###############################################################################
max_temp = Label(window, text="Max Temp: ", font=("Inter", 15, "bold"), justify='left')
max_temp.place(x=0,y=200,height=40,width=150)
max_tempCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
max_tempCurrent.place(x=150,y=200,height=40,width=350)
###############################################################################
pressure = Label(window,text="Pressure: ", font=("Inter", 15, "bold"), justify='left')
pressure.place(x=0,y=240,height=40,width=150)
pressureCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
pressureCurrent.place(x=150,y=240,height=40,width=350)
###############################################################################
humidity = Label(window,text="Humidity: ", font=("Inter", 15, "bold"), justify='left')
humidity.place(x=0,y=280,height=40,width=150)
humidityCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
humidityCurrent.place(x=150,y=280,height=40,width=350)
###############################################################################
visibility = Label(window,text="Visibility: ", font=("Inter", 15, "bold"), justify='left')
visibility.place(x=0,y=320,height=40,width=150)
visibilityCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
visibilityCurrent.place(x=150,y=320,height=40,width=350)
###############################################################################
cloud = Label(window,text="Cloud: ", font=("Inter", 15, "bold"), justify='left')
cloud.place(x=0,y=360,height=40,width=150)
cloudCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
cloudCurrent.place(x=150,y=360,height=40,width=350)
###############################################################################
wind = Label(window,text="Wind: ", font=("Inter", 15, "bold"), justify='left')
wind.place(x=0,y=400,height=40,width=150)
windCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
windCurrent.place(x=150,y=400,height=40,width=350)
###############################################################################
sunrise = Label(window,text="Sunrise: ", font=("Inter", 15, "bold"), justify='left')
sunrise.place(x=0,y=440,height=40,width=150)
sunriseCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
sunriseCurrent.place(x=150,y=440,height=40,width=350)
###############################################################################
sunset = Label(window,text="Sunset: ", font=("Inter", 15, "bold"), justify='left')
sunset.place(x=0,y=480,height=40,width=150)
sunsetCurrent = Label(window, font=("Inter", 15, "bold"), justify='left')
sunsetCurrent.place(x=150,y=480,height=40,width=350)
###############################################################################
###################################################################################
#main loop
window.mainloop()