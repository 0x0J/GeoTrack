#Licensed under GPLv3.0
#built by 0x0J

import tkinter as tk
import requests
import tkinter.font as font

#set size of app

HEIGHT = 720
WIDTH = 720

#response format from API

def format_response(query):
	try:
		asp = query['as']
		city = query['city']
		country = query['country']
		countrycode = query['countryCode']
		lat = query['lat']
		lon = query['lon']
		region = query['regionName']
		timezone = query['timezone']
		zip = query['zip']



		final_str = 'AS: %s \nCity: %s \nCountry: %s \nCountry Code: %s \nLat: %s \nLon: %s \nRegion: %s\nTimezone: %s\nZip: %s' % (asp, city, country, countrycode, lat, lon, region, timezone, zip)

	#Print API request

	except:
		final_str = 'A problem occured.'

#print error if unable to complete API call

	return final_str


def get_ip(query):
	url = 'http://ip-api.com/json/' +query
	response = requests.get(url)
	query = response.json()
# API query

	label['text'] = format_response(query)




root = tk.Tk()

root.title('GeoTrack')

#sets title of tkinter window

thefont = font.Font(family='Helvetica', size=20, weight='bold')
#font used for button

thefont2 = font.Font(family='Times', size=20, weight='bold')
#Font used for label



canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
#sets canvas height and width

background_image = tk.PhotoImage(file='bg.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
#sets and places background image (bg.png)

frame = tk.Frame(root, bg='black', bd=5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')
#places frame as well as configs

button = tk.Button(frame, text="GeoTrack", font=40, bg='black', fg='white', command=lambda: get_ip(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)
#places button as well as config/name. Lambda sends a loop to get_ip function once button is pressed

button['font'] = thefont
#font used for button

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)
#places frame

lower_frame = tk.Frame(root, bg='blue', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
#places lower frame

label = tk.Label(lower_frame, bg='white')
label.place(relheight=1, relwidth=1)
label['font'] = thefont2
#places label inside the lower frame
#sets font to thefont2

root.mainloop()
