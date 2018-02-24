# Práctica 1: Estación de monitoreo de clima

Alan Badillo Salas (badillo.soft@hotmail.com)

## Introducción

Una estación de monitoreo de clima consiste en una aplicación en la que el usuario pueda monitorear valores de humedad y temperatura extraídos de diversos sensores colocados a lo largo de uno o varios dispositivos `IoT`. Está estación de monitoreo, tiene la cualidad de ser económica y eficiente, y puede ser instalada en cualquier habitación o zona que cuente con conexión a internet y corriente eléctrica.

En está práctica vamos a montar una estación de monitoreo de clima en una `Raspberry Pi` utilizando sensores `DHT11` de humedad y temperatura.

Primero construiremos un `Web API` capaz de escribir y leer los valores de los sensores para poder monitorear los datos con gráficas sencillas.

Posteriormente haremos que las lecturas registradas por los sensores conectados manden los datos a nuestro `Web API` para poder monitorearlo desde cualquier web.

## Paso 1. Conectar la `Raspberry Pi` a internet

Primero necesitamos conectar nuestra `Raspberry Pi` a internet, para poder manipularla desde cualquier lugar. Para esto utilizaremos `Dataplicity` que es una plataforma de acceso remoto para `IoT`.

Lo primero que debemos hacer es registrar una cuenta en https://www.dataplicity.com/features/.

Una vez creada la cuenta, debemos registrar el dispositivo `Raspberry Pi` dando clic en `+ Add new device` en el panel principal, lo cual generará un comando `bash` que deberemos escribir en la `Raspberry Pi`, similar al siguiente:

> curl https://www.dataplicity.com/XXXXXXXX.py | sudo python

Donde `XXXXXXXX` es el código para activar la raspberry como parte de tus dispositivos.

Una vez activada la `Raspberry Pi` podremos acceder a esta desde cualquier sitio. Para ingresar con el usuario `pi` deberemos escribir en la terminal web `$ su pi` e ingresar la contraseña (`raspberry` por defecto).

Es importante activar la opción `Wormhole` para generar un vínculo único a nuestro servidor montado en la `Raspberry Pi`, similar a `https://**********.dataplicity.io/` donde `**********` es el id único de nuestro dispositivo.

## Paso 2. Montar un servidor de prueba

Si nosotros ingresamos a `https://**********.dataplicity.io/` seguramente veremos un mensaje que dice que nuestro servicio no responde, esto se debe a que no hay ningún servidor ejecutandose en nuestro dispositivo.

Lo primero que debemos hacer es crear un script de python que contenga un servidor de prueba, para comprobar que nuestro dispositivo este funcionando:

> /server_test.py

~~~py
from from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "dispositivo funcionando :D"
app.run(port=80)
~~~

Si ejecutamos el script mediante `$ sudo python server_test.py` podremos ingresar a `https://**********.dataplicity.io/` y ver el resultado.

> __IMPORTANTE:__ Ejecuta el script en modo `sudo`, de otra forma no se ejecutará y causará que se bloquee la `Raspberry Pi` hasta reiniciarla manualmente.

## Paso 3. Crear un sensor que simule al sensor `DHT11`

Lo primero que haremos será simular un sensor y la lectura de sus datos cada sengundo mediante un hilo.

> /sensor_simulator.py

~~~py
from threading import Thread
import random
import time

# Ultimos valores leidos del sensor
humidity = 0
temperature = 0
valid = False

# Buffer con los ultimos 100 valores leidos
humidity_buff = []
temperature_buff = []

# Indicamos si el hilo esta ejecutandose
running = False

# Tarea encargada de leer los datos del sensor (sera ejecutada en un hilo)
def task():
    # Indicamos que vamos a reasignar las variables globales
    global humidity, temperature, valid

    # Creamos un ciclo hasta que se force la detencion
    while running:
        # La lectura sera valida 90% de las veces
        valid = random.random() < 0.9

        # Si la lectura es valida actualizamos los valores
        if valid:
            humidity = random.uniform(0, 100)
            temperature = random.uniform(0, 100)

        # Agregamos los valores al buffer
        humidity_buff.append(humidity)
        temperature_buff.append(temperature)

        # Limitamos a 100 valores los buffers
        if len(humidity_buff) > 100:
            humidity_buff.pop(0)
        if len(temperature_buff) > 100:
            temperature_buff.pop(0)

        print("DTH11/SIM: H={:.2f} T={:.2f} V={}".format(humidity, temperature, valid))

        # Dormimos la lectura del sensor 1 segundo
        time.sleep(1)

# Creamos una funcion para iniciar el hilo
def start():
    global running

    if running:
        print("DTH11/SIM is running")
        return

    running = True
    thread = Thread(target=task)
    thread.start()

# Creamos una funcion que forza la detencion del hilo
def stop():
    global running
    running = False

# Si ejecutamos este archivo localmente inciamos el hilo
if __name__ == "__main__":
    start()
~~~

## Paso 4. Crear un `Web API` real que muestre los datos del sensor

Para crear el `Web API` deberemos establecer las siguientes rutas descritas:

~~~txt
GET /api/sensor/humidity -- Obtiene el último valor de humedad
GET /api/sensor/temperature -- Obtiene el último valor de temperatura
GET /api/sensor/humidity/buffer -- Obtiene el buffer con los valores de humedad
GET /api/sensor/temperature/buffer -- Obtiene el buffer con los valores de temperatura
~~~

> /server.py

~~~py
from flask import Flask
import sensor_simulator as sensor
import json

app = Flask(__name__)

# Iniciamos la lectura del sensor (se ejecuta en paralelo)
sensor.start()

@app.route("/")
def home():
    return """
        GET /api/sensor/humidity -- Obtiene el último valor de humedad<br>
        GET /api/sensor/temperature -- Obtiene el último valor de temperatura<br>
        GET /api/sensor/humidity/buffer -- Obtiene el buffer con los valores de humedad<br>
        GET /api/sensor/temperature/buffer -- Obtiene el buffer con los valores de temperatura
    """

# Definimos las rutas del Web API

@app.route("/api/sensor/humidity")
def sensor_humidity():
    # Obtenemos el valor de humedad del sensor y lo devolvemos (como string)
    return "{:.2f}".format(sensor.humidity)

@app.route("/api/sensor/temperature")
def sensor_temperature():
    return "{:.2f}".format(sensor.temperature)

@app.route("/api/sensor/humidity/buffer")
def sensor_humidity_buff():
    # Enviamos la lista (el buffer) en el formato JSON
    return json.dumps(sensor.humidity_buff)

@app.route("/api/sensor/temperature/buffer")
def sensor_temperature_buff():
    return json.dumps(sensor.temperature_buff)

app.run(port=80)
~~~

## Paso 5. Crear una plantilla de monitoreo

Para visualizar mejor los datos vamos a crear una plantilla para visualizar los datos de una forma más cómoda:

> /templates/monitor.html

~~~html
<div class="card">
    <span class="city">Monitor de Clima</span>
    <ul class="menu">
        <li></li>
        <li></li>
        <li></li>
    </ul>
    <br>
    <div class="temp2">{{ humidity }}&#176;</div>
    <span class="temp">{{ temperature }}&#176;</span>
    <span>
        <ul class="variations">
            <li id="humidity_desc">SECO</li>
        </ul>
    </span>
    <div class="forecast clear">
        <div id="humidity_list" class="day tue">HUMEDAD
            <br>
            <span class="highTemp">79&#176;</span>
            <br>
            <span class="lowTemp">57&#176;</span>
            <br>
            <span class="lowTemp">57&#176;</span>
        </div>
        <div id="temperature_list" class="day wed">TEMPERATURA
            <br>
            <span class="highTemp">79&#176;</span>
            <br>
            <span class="lowTemp">57&#176;</span>
            <br>
            <span class="lowTemp">57&#176;</span>
        </div>
    </div>
</div>

<script>
    window.onload = function() {
        const humidity_buff = {{ humidity_buff | safe }};
        const h = humidity_buff.length;

        const humidity_list = document.getElementById("humidity_list");

        humidity_list.innerHTML = `HUMEDAD<br>
            <span class="highTemp">${(humidity_buff[h - 1] || 0).toFixed(1)}&#176;</span> <br>
            <span class="lowTemp">${(humidity_buff[h - 2] || 0).toFixed(1)}&#176;</span> <br>
            <span class="lowTemp">${(humidity_buff[h - 3] || 0).toFixed(1)}&#176;</span>
        `;

        const temperature_buff = {{ temperature_buff | safe }};
        const t = temperature_buff.length;

        const temperature_list = document.getElementById("temperature_list");

        temperature_list.innerHTML = `HUMEDAD<br>
            <span class="highTemp">${(temperature_buff[t - 1] || 0).toFixed(1)}&#176;</span> <br>
            <span class="lowTemp">${(temperature_buff[t - 2] || 0).toFixed(1)}&#176;</span> <br>
            <span class="lowTemp">${(temperature_buff[t - 3] || 0).toFixed(1)}&#176;</span>
        `;

        setTimeout(function () {
            window.location.reload();
        }, 5000); 
    }
</script>

<style>
    body {
        background: #dbdbdb;
    }

    .clear {
        clear: both;
    }

    .card {
        width: 25em;
        min-height: 22.5em;
        background: #fff;
        margin: 2em auto;
        border-radius: .2em;
        padding-top: 1em;
        padding-left: 1em;
        padding-right: 1em;
    }

    .city {
        font-family: Roboto;
        font-weight: 300;
        font-size: 1.8em;
        color: #5b5b5b;
    }

    .menu {
        float: right;
        font-family: Roboto;
        font-size: .5em;
        color: #5b5b5b;
        margin-top: -.09em;
        margin-right: -2em;
        list-style: square;
    }

    .sun {
        width: 4em;
        height: 4em;
        border-radius: 2.5em;
        background: #FBD80A;
        margin-top: 1em;
    }

    .temp2 {
        width: 4em;
        margin-top: 1em;
        font-size: 3em;
        color: #777;
    }

    .temp {
        float: right;
        font-family: Roboto;
        font-weight: 300;
        font-size: 8.5em;
        margin-top: -.75em;
        color: #5b5b5b;
    }

    .variations {
        font-family: Roboto;
        font-wight: 300;
        color: #8c8c8c;
        list-style: none;
        margin-left: -2em;
    }

    .mph {
        font-size: .8em;
    }

    .forecast {
        width: 100%;
        margin: 0 auto;
    }

    .day {
        display: block;
        width: 44%;
        height: 9em;
        float: left;
        margin: 0 .375em .5em;
        text-align: center;
        font-family: Roboto;
        color: #5b5b5b;
        border-right: .1em solid #d9d9d9;
        line-height: 2;
    }

    .fri {
        border-right: none;
    }

    .highTemp {
        font-weight: bold;
    }

    .lowTemp {
        color: #8c8c8c;
    }
</style>
~~~

> /server.py

~~~py
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
    return render_template("monitor.html",
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
~~~

Hasta aquí ya tenemos un sistema de monitore funcional que nos muestra la humedad y temperatura simulados en nuestro dispositivo. Ahora es tu turno de continuar la práctica para enlazar los valores reales leídos por el sensor.

## PROBLEMA 1. Leer los datos del sensor real

* Conecta el sensor `DHT11` a la `Raspberry Pi`
* Utiliza el módulo `dht11.py` para leer los datos de humedad y temperatura del sensor `DHT11`
* Crea un módulo llamado `sensor_real.py` basado en `sensor_simulator.py` que obtenga los datos reales del sensor en lugar de números aleatorios
* Comprueba que el servidor funcione

## PROBLEMA 2. Control de clima (opcional)

* Crea una ruta `API` en el servidor que indique un estado de la humedad, por ejemplo, `SECO TEMPLADO HUMEDO` y también para la temperatura, por ejemplo, `FRIO AMBIENTE CALIDO EXTREMO`.
* Intenta integrar está gráfica de tipo `D3.js`: http://bl.ocks.org/ameyms/9184728

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