import tkinter as tk
import requests

Height = 500
Width = 600


def trigger(entry):
    print("This is the entry", entry)  # Used function to check if button's been pressed

# e0fbe9c3531609ff52c56c521b3907ab
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}


def format(weather):
    name = weather['name']
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']

    return str(name) + '' + str(desc) + '' + str(temp)


def get_weather(city):
    weather_key = "e0fbe9c3531609ff52c56c521b3907ab"
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"APPID": weather_key, "q": city, "units": "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format(weather)


root = tk.Tk()  # This is to make the actual blank border window. Places everything into this window

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

background_image = tk.PhotoImage(file="weathergui.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Wanted the picture to take up all the space.

frame = tk.Frame(root, bg="#90d1fe", bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor="n")  # Sets relative height/width for the frame. The numbers represent the % of the screen it covers. Used anchor=n to place relx at the top for 0.5.

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text="Get Weather", font=10, command=lambda: get_weather(entry.get()))  # To create button. Like a nested structure where the root creates everything
button.place(relx=0.7, relwidth=0.3, relheight=1)  # can use either place, pack or grid. Place seems to be the most easiest to use for me.
# set relx to 0.7 as the entry width is 0.65 so to create space i chose 0.7

lower_frame = tk.Frame(root, bg="#90d1fe", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")
# Used relx=0.5 so that this frame which is going to output data is centered, also made the anchor north for this to happen

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)  # This label is going to be used to output data, hence made it the whole size of the lower frame

root.mainloop()  # runs application
