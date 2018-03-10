import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template

io = socketio.Server()
app = Flask(__name__)

@app.route('/')
def index():
    return "Hola socket io"

@io.on('connect')
def connect(uid, environ):
    print("connect ", uid)

@io.on('message')
def message(uid, event, data):
    print("message ", event, data)
    io.emit('reply', { "message": "ok", "id": uid })

@io.on('disconnect')
def disconnect(uid):
    print('disconnect ', uid)

# wrap Flask application with engineio's middleware
app = socketio.Middleware(io, app)

# deploy as an eventlet WSGI server
eventlet.wsgi.server(eventlet.listen(('localhost', 8000)), app)