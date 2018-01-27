from flask import Flask
import threading
import time
import random
import json

app = Flask(__name__)

distancia = -1
log = []

def leer_distancia():
    global distancia
    while True:
        distancia = random.uniform(10, 100)
        log.append(distancia)
        while len(log) > 100:
            log.pop(0)
        print("la distancia es: {} cm".format(distancia))
        time.sleep(0.5)

print("Tareas iniciadas...")
threading.Thread(target=leer_distancia).start()

@app.route("/sensor/distancia")
def sensor_distancia():
    return str(distancia)

@app.route("/sensor/distancia/log")
def sensor_distancia_log():
    return json.dumps(log)

print("iniciando servidor...")
app.run()