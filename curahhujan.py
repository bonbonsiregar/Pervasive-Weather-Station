import glob
from gpiozero import DigitalInputDevice

from time import sleep
import json
import os
import datetime
import threading
import pyrebase

config = {
	"apiKey": "AIzaSyCJkHYj184yxV6BCJRpCq_yBWNyuO13iAo",
    	"authDomain": "apakek-9466d.firebaseapp.com",
    	"databaseURL": "https://apakek-9466d.firebaseio.com",
    	"projectId": "apakek-9466d",
    	"storageBucket": "apakek-9466d.appspot.com",
    	"messagingSenderId": "1038369229659"
	}

firebase = pyrebase.initialize_app(config)

rain_sensor = DigitalInputDevice(5)
count = 0
bucket = 1.346
buckettotal = 0
current_state = True
previous_state = True

def kirimdatabase():
	global buckettotal
	global count
        threading.Timer(15.0, kirimdatabase).start()
	db = firebase.database()

        data = {"curahHujan ": buckettotal}
	data2 = {"akumulasiHujan" : buckettotal}
	db.child("sensor/").child("Hujan").push(data)
	db.child("sensor/").child("akumulasiHujan").set(data2)
	count = 0

kirimdatabase()

while (1):

	current_state = rain_sensor.value

	if previous_state == True and current_state == False:

		count =  count + 1
		buckettotal = count * bucket
		print (buckettotal)
	previous_state = current_state
