from time import sleep
import datetime
from firebase import firebase
import Adafruit_DHT

#import urllib2, urllib, httplib
import json
import os
from functools import partial
import pyrebase

#GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()
#GPIO.setwarnings(False)

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
#https://apakek-9466d.firebaseio.com/sensor = Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT11
# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
pin = 17



firebase = firebase.FirebaseApplication('https://apakek-9466d.firebaseio.com/')
config = {
        "apiKey": "AIzaSyCJkHYj184yxV6BCJRpCq_yBWNyuO13iAo",
        "authDomain": "apakek-9466d.firebaseapp.com",
        "databaseURL": "https://apakek-9466d.firebaseio.com",
        "projectId": "apakek-9466d",
        "storageBucket": "apakek-9466d.appspot.com",
        "messagingSenderId": "1038369229659"
        }

firebase2 = pyrebase.initialize_app(config)



def update_firebase():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
		sleep(5)
		str_temp = ' {0:0.2f} *C '.format(temperature)	
		str_hum  = ' {0:0.2f} %'.format(humidity)
		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))	

	else:
		print('Failed to get reading. Try again!')	
		sleep(10)

	data = {"temp": temperature,"humidity": humidity} 
	firebase.put('/sensor/dht','dht',data)
	db = firebase2.database()


        data2 = {"Temperature":temperature, "Humidity" : humidity}
        db.child("sensor/dht").child("dht11").push(data2)

while True:
		update_firebase()
		break
