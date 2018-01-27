from flask import Flask
import threading
import time
import random

app = Flask(__name__)

distancia = -1

def leer_distancia():
    global distancia
    while True:
        distancia = random.uniform(10, 100)
        print("la distancia es: {} cm".format(distancia))
        time.sleep(1)

print("Tareas iniciadas...")
threading.Thread(target=leer_distancia).start()

@app.route("/sensor/distancia")
def sensor_distancia():
    return str(distancia)

print("iniciando servidor...")
app.run()