# Práctica 2: Control Remoto de Dispositivos

Alan Badillo Salas (badillo.soft@hotmail.com)

## Introducción

Lo más interesante en IoT no es poder medir sensores y obtener datos desde una terminal remota, sino, por el contrario, poder manipular los dispositivos IoT desde cualquier lugar. Para poder hacer control remoto, debemos establecer un sistema de comunicación preciso entre el cliente (la interfaz web) y el servidor (la raspberry).

Sin embargo, crear un servidor `Flask` no nos ayuda mucho, dado que el servidor no tiene una comunicación directa con el cliente, es decir, hasta que el cliente realice una petición, el servidor no podrá enviarle un mensaje al cliente, es por esto que utilizaremos `Socket.IO` para poder lograr una comunicación dual cliente-servidor.

Lo primero que realizaremos será montar un servidor `socket.io` junto a `flask`, para posteriormente enviar y recibir mensajes. Finalmente tendrás que utilizar tus conocimientos sobre actuadores para poder resolver los problemas de la práctica.

## Paso 1. Montar un Servidor `SocketIO`

Primero deberemos instalar adicional a `flask`, los módulos `python-socketio` y `eventlet` mediante `pip` (`pip install python-socketio eventlet`).

Luego deberemos crear un servidor en un puerto deseado como ya lo sabemos hacer, integrando `socket.io` como en el siguiente código:

~~~py
# Importamos la libreria Flask
from flask import Flask
# Importamos las librerias adicionales socketio y eventlet
import socketio
import eventlet
import eventlet.wsgi

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
    # Cada que recibimos un mensaje obtenemos el evento y los datos
    print("message ", event, data)
    # Contestamos el mensaje mediante el evento `reply`
    io.emit('reply', { "message": "ok", "id": uid })

# Definimos el evento `disconnect` de socket.io
@io.on('disconnect')
def disconnect(uid):
    print('disconnect ', uid)

# Unimos el servidor socket.io (io) con el servidor flask (app)
app = socketio.Middleware(io, app)

# Montamos ambos servidores mediante eventlet
eventlet.wsgi.server(eventlet.listen(('localhost', 8000)), app)
~~~

## Paso 2. Crear un cliente web para socket.io

Para mandar algunos mensajes a nuestro servidor vamos a crear una pequeña interfaz web que consuma nuestro servidor `socket.io` creado en python.

~~~html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Cliente</title>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/2.0.4/socket.io.js"></script>
    <script>
        window.onload = () => {
            // Creamos un cliente socket.io (el servidor está montado en http://localhost:8000)
            const socket = io('http://localhost:8000');

            // Configuramos el evento `connect`
            socket.on('connect', () => {
                console.log("Conectado");
            });

            // Configuramos el evento `reply`
            socket.on('reply', data => {
                console.log("Respuesta:", data);
            });

            // Configuramos el evento `connect`
            socket.on('disconnect', () => {
                console.log("Desconectado");
            });

            // Enviamos algunos mensajes
            socket.send("evento_1", "Hola mundo");
            socket.send("evento_2", { a: 123, b: true });
        };
    </script>
</body>
</html>
~~~

## PROBLEMA 1. Crear un chat

* Crea una interfaz web que contenga una lista para agregar los mensajes recibidos.
* También agrega una caja de texto y un botón para que cada que el botón se pulsa envie el mensaje al servidor.
* En el servidor se debe replicar el mismo mensaje.
* Agrega la lógica necesaria para que cada que se recibe un mensaje del servidor lo agregue en la lista.

## PROBLEMA 2. Crear un controlador de Relés

* Crea una interfaz web con dos botones, uno que envie al servidor el evento `prender` y otro que envie el evento `apagar`.
* Configura el servidor para que al recibir el evento `prender` encienda el relé y al recibir el evento `apagar` lo apague.
* Sustituye en la interfaz los botones por dos imágenes, una donde se muestre un foco encendido y otra donde se muestre un foco apagado.

<hr>

El reporte deberá consistirá en un documento PDF que contenga como título el número de práctica y nombre, seguido del nombre de los integrantes con correo incluído. En el cuerpo de la práctica se deberán colocar paso a paso los procedimientos efectuados para resolver los problemas de la práctica y deberá incluir imágenes (capturas de pantalla o fotos).

Ejemplo:

~~~txt
Practica X: Robot Buscaminas

Ana Baez (ana@gmail.com)
Juan Baez (juan@gmail.com)

Problema 1: Encontrar la mina oculta

Paso 1. Conectamos el sensor de distancia al sensor

*IMAGEN DEL CABLEADO*

Paso 2. Programamos la función de rastreo

*CAPTURA DE PANTALLA DEL CÓDIGO*

Paso 3. Colocamos la mina

*FOTO*

Paso 4. Activamos al robot de forma remota

*CAPTURA DE PANTALLA DE LOS COMANDOS USADOS*

Paso 5. Verificamos que el robot llego a la mina

*IMAGEN DEL ROBOT SOBRE LA MINA*
~~~