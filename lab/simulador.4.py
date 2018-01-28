# -*- coding: utf-8 -*-
from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from StringIO import StringIO

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
        #print("la distancia es: {} cm".format(distancia))
        time.sleep(0.5)

print("Tareas iniciadas...")
threading.Thread(target=leer_distancia).start()

@app.route("/sensor/distancia")
def sensor_distancia():
    return str(distancia)

@app.route("/sensor/distancia/log")
def sensor_distancia_log():
    return json.dumps(log)

@app.route("/sensor/distancia/grafica")
def sensor_distancia_grafica():
    # Creamos una figura de imagen
    fig = Figure()

    # Creamos un lienzo donde graficar dentro de la figura
    ax = fig.add_subplot(111)
    
    # Dibujamos la grafica
    ax.plot(range(len(log)), log, '-')
    
    # Creamos un canvas para convertir la figura en una imagen PNG
    canvas = FigureCanvas(fig)
    
    # Creamos un objeto donde colocar la imagen como texto
    png_output = StringIO()

    # Convertimos la imagen en texto dentro del objeto
    canvas.print_png(png_output)
    
    # Obtenemos la respuesta que será enviada al usuario a partir del texto de la imagen
    response = make_response(png_output.getvalue())
    
    # Indicamos al navegador que se trata de una imagen PNG
    response.headers['Content-Type'] = 'image/png'
    
    # Enviamos la imagen
    return response

print("iniciando servidor...")
app.run()