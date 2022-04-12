import os
from time import sleep
import Adafruit_ADS1x15
import glob
import time
from time import sleep
import datetime
from firebase import firebase

firebase = firebase.FirebaseApplication('https://apakek-9466d.firebaseio.com/', None)

adc = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)

GAIN = 2/3

volts = 0

while 1:

	value = adc.read_adc (2, gain=GAIN)
	volts = (value * 0.1875) / 1000
	led0 = 0
	led1 = 1
	led2 = 2
	led3 = 3

	print(value)
	print("%.2f" % volts)

	if volts < 2.30:
		print("0 LED")
       		data = {"power": led0}
        	firebase.put('/sensor','battery',data)
	if volts >= 2.30 and volts < 2.85:
		print("1 LED")
		data = {"power": led1}
		firebase.put('/sensor','battery',data)
	if volts >= 2.85 and volts < 3.37:
		print("2 LED")
		data = {"power": led2}
		firebase.put('/sensor','battery',data)
	if volts >= 3.37:
		print("3 LED")
		data = {"power": led3}
		firebase.put('/sensor','battery',data)

	break;
