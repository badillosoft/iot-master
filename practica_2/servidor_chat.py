from flask import Flask
import socketio
import eventlet
import eventlet.wsgi
import time

# Creamos un servidor Flask
app = Flask(__name__)

# Creamos un servidor SocketIO
io = socketio.Server()

# Definimos las rutas Flask tradicionales
@app.route('/')
def index():
    return "Hola socket io"

# Definimos el evento `connect` de socket.io
@io.on('connect')
def connect(uid, environ):
    print("connect ", uid)

# Definimos el evento `message` de socket.io
@io.on('message')
def message(uid, event, data):
    text = "{}: {} {}".format(uid, data, time.strftime("%d/%m/%Y %H:%M:%S"))
    io.emit('evento_3', text)

# Definimos el evento `disconnect` de socket.io
@io.on('disconnect')
def disconnect(uid):
    print('disconnect ', uid)

# Unimos el servidor socket.io (io) con el servidor flask (app)
app = socketio.Middleware(io, app)

# Montamos ambos servidores mediante eventlet
eventlet.wsgi.server(eventlet.listen(('localhost', 8000)), app)