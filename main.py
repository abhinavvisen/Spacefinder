#!/bin/python3

from urllib import request
import json
import turtle


#storing the url in a variable
weburl = 'http://api.open-notify.org/astros.json'

#reading the url page or API page on the variable
response = request.urlopen(weburl)

#Loading the data

api1 = json.loads(response.read())

print('Number of astronauts in space are:- ', api1['number'])

#Storing the data and displaying it in the proper format.
astro = api1['people']

for a in astro:
    print('Name of the astronaut:-', a['name'])

#loading and storing the API URL IN THE VARIABLE

weburl = 'http://api.open-notify.org/iss-now.json'
#READING THE DATA
response = request.urlopen(weburl)
api2 = json.loads(response.read())

point = api2['iss_position']

latitude = point['latitude']
longitude = point['longitude']

#Displaying the latitude and longitude of the ISS
print('Current latitude:- ', latitude)
print('Current longitude:- ', longitude)

#Resizing the image according to the screen
screen = turtle.Screen()
screen.setup(720, 360)
screen.bgpic('worldmap.jpg')

#Loading a pointer
screen.register_shape('pointer.gif')
station = turtle.Turtle()
station.shape('pointer.gif')
station.setheading(90)

#setting the position of pointer according to the latitude and longitude of the current ISS
station.setpos(float(latitude),float(longitude))

turtle.done()




