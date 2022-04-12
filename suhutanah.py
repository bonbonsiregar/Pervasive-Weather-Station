from time import sleep
from w1thermsensor import W1ThermSensor
from firebase import firebase
import pyrebase

firebase = firebase.FirebaseApplication('https://apakek-9466d.firebaseio.com')
config = {
        "apiKey": "AIzaSyCJkHYj184yxV6BCJRpCq_yBWNyuO13iAo",
        "authDomain": "apakek-9466d.firebaseapp.com",
        "databaseURL": "https://apakek-9466d.firebaseio.com",
        "projectId": "apakek-9466d",
        "storageBucket": "apakek-9466d.appspot.com",
        "messagingSenderId": "1038369229659"
        }

firebase2 = pyrebase.initialize_app(config)


sensor = W1ThermSensor()

while True:
	temperature_in_celsius = sensor.get_temperature()
	print temperature_in_celsius
	data = {"temp(c)": temperature_in_celsius}
	db = firebase2.database()

        data2 = {"temperatur(c)": temperature_in_celsius}
        db.child("sensor/ds18b20").child("dsbTemp").push(data2)
	firebase.put('/sensor/ds18b20','soilTemp',data)
	break
#	sleep(2)


#temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
#temperature_in_all_units = sensor.get_temperatures([
#    W1ThermSensor.DEGREES_C,
#    W1ThermSensor.DEGREES_F,
#    W1ThermSensor.KELVIN])
