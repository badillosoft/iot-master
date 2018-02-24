from flask import Flask
import sensor_simulator as sensor
import json

app = Flask(__name__)

sensor.start()

@app.route("/")
def home():
    return """
        GET /api/sensor/humidity -- Obtiene el último valor de humedad<br>
        GET /api/sensor/temperature -- Obtiene el último valor de temperatura<br>
        GET /api/sensor/humidity/buffer -- Obtiene el buffer con los valores de humedad<br>
        GET /api/sensor/temperature/buffer -- Obtiene el buffer con los valores de temperatura
    """

@app.route("/api/sensor/humidity")
def sensor_humidity():
    return "{:.2f}".format(sensor.humidity)
    
@app.route("/api/sensor/humidity/buffer")
def sensor_humidity_buff():
    return json.dumps(sensor.humidity_buff)

@app.route("/api/sensor/temperature")
def sensor_temperature():
    return "{:.2f}".format(sensor.temperature)

@app.route("/api/sensor/temperature/buffer")
def sensor_temperature_buff():
    return json.dumps(sensor.temperature_buff)

app.run()