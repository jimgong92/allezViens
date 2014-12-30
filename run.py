# from flask import Flask, request
# import os.path

# app.run()
from flask import Flask, request
import json
import requests
import connect
app = Flask(__name__, static_folder='client', static_url_path='')

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/driver', methods=['GET', 'POST'])
def drivers():
	if (request.method == 'GET'):
		data = json.loads(request.data)
		origin = data['origin']
		destination = data['destination']
		temp = connect.findDrivers(origin, destination)
		return str(temp)
	if (request.method == 'POST'):
		if (request.headers['Content-Type'] == 'application/json'):
			data = json.loads(request.data)
			if (data['type'] == 'create'):
				print(data)
				connect.createDriver(data['origin'], data['destination'], data['id'])
				return 'Driver added to database'

			#TODO: HANDLE PICKS
			if (data['type'] == 'pick'):
				print(data)
				connect.pickPassenger(data['driverID'], data['passengerID'])
				return 'Successful pick'


@app.route('/passenger', methods=['GET', 'POST'])
def passengers():
	if (request.method == 'GET'):
		data = json.loads(request.data)
		origin = data['origin']
		destination = data['destination']
		temp = connect.findPassengers(origin, destination)
		return str(temp)
	if (request.method == 'POST'):
		if (request.headers['Content-Type'] == 'application/json;charset=UTF-8'):
			data = json.loads(request.data)
			if (data['type'] == 'create'):
				connect.createPassenger(data['origin'], data['destination'], data['id'])
				return 'Passenger added to database'

			#TODO: HANDLE PICKS
			if (data['type'] == 'pick'):
				connect.pickDriver(data['passengerID'], data['driverID'])
				return 'Successful pick'


if (__name__ == '__main__'):
    app.run()