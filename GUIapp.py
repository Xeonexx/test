# Yash Shrimali
# Gui attempt(s)

import tkinter as tk
import requests

Height = 500
Width = 800


def test_function(entry):
	print("This is the entry:", entry)


# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# e0fbe9c3531609ff52c56c521b3907ab


def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (C): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str


def get_weather(city):
	weather_key = 'e0fbe9c3531609ff52c56c521b3907ab'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	param = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params=param)
	weather = response.json()

	label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width=Width)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#90d1ef', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')  # The search bar frame


lower_frame = tk.Frame(root, bg='#90d1ef', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.6, relheight=0.5, anchor='n')  # The output frame


even_lower_frame = tk.Frame(root, bg='green', bd=3)
even_lower_frame.place(relx=0.01, rely=0.94, relwidth=0.25, relheight=0.05)  # Credits frame


label2 = tk.Label(even_lower_frame, text='Made by: Yash Shrimali', bg='cyan')  # Label for even_lower_frame
label2.place(relwidth=1, relheight=1)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)  # Enables the search bar and makes it interactable

button = tk.Button(frame, text="Get Weather", font=80, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


label = tk.Label(lower_frame, bg='#f3ff87')
label.place(relwidth=1, relheight=1)  # for output frame
label.config(font=40)

weather_icon = tk.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=0.9, rely=0, relwidth=1, relheight=0.2)


root.mainloop()
