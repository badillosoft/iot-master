from flask import Flask, render_template
import sensor_simulator as sensor
import json

app = Flask(__name__)

sensor.start()

@app.route("/api/sensor/start")
def sensor_start():
    sensor.start()
    return "sensor started"

@app.route("/api/sensor/stop")
def sensor_stop():
    sensor.stop()
    return "sensor stopped"

@app.route("/")
def home():
    return render_template("humedad.html",
        humidity=int(sensor.humidity),
        temperature=int(sensor.temperature),
        valid=sensor.valid,
        humidity_buff=sensor.humidity_buff,
        temperature_buff=sensor.temperature_buff)

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

app.run(port=80)