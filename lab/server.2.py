# -*- coding: utf-8 -*-
from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from StringIO import StringIO

app = Flask(__name__)

@app.route("/imagen")
def imagen():
    # Creamos una figura de imagen
    fig = Figure()

    # Creamos un lienzo donde graficar dentro de la figura
    ax = fig.add_subplot(111)
    
    # Dibujamos la grafica
    ax.plot([1, 2, 3, 4, 5], [3, 6, 4, 2, 8], '-')
    
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

app.run()