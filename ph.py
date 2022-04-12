import os
from time import sleep
import Adafruit_ADS1x15
import glob
import time
from time import sleep
import datetime
from firebase import firebase
import pyrebase

firebase = firebase.FirebaseApplication('https://apakek-9466d.firebaseio.com/', None)
config = {
        "apiKey": "AIzaSyCJkHYj184yxV6BCJRpCq_yBWNyuO13iAo",
        "authDomain": "apakek-9466d.firebaseapp.com",
        "databaseURL": "https://apakek-9466d.firebaseio.com",
        "projectId": "apakek-9466d",
        "storageBucket": "apakek-9466d.appspot.com",
        "messagingSenderId": "1038369229659"
        }

firebase2 = pyrebase.initialize_app(config)


adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 2/3

volts = 0.0

while 1:
	value = 0
        value = adc.read_adc(0, gain=GAIN)

        volts = value / 32767.0 * 6.144

	hitung = (-18.75*volts)+15.53
	db = firebase2.database()

        data2 = {"calculate": "%.2f" % hitung}
        db.child("sensor").child("phTanah").push(data2)

        data = {"hitung": "%.2f" % hitung}
        firebase.put('/sensor','pHTanah',data)
        print(value)
        print("%.2f" % hitung)
	break
