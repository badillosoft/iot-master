# Sensores

Por Alan Badillo Salas (badillo.soft@hotmail.com)

## Introducción

Un sensor es el medio en el que se recolecta información entre el entorno y la raspberry. Un sensor de luz por ejemplo, consiste en un foto-resistor que varía el voltaje dependiendo de la intensidad de luz que reciba. Existen diversos tipos de sensores, pero su objetivo es evidente, permiten interpretar el entorno a través de números, esos números tienen un significado y varían de acuerdo a un significado, por ejemplo, nivel de temperatura, nivel de humedad, proximidad de un objeto, intensidad de luz, intensidad de sonido. Sin embargo, los sensores crean una realidad limitada a su precisión y no son capaces de formar un contexto completo, por ejemplo, un robot que posee un sensor de distancia al frente ignora como es el objeto que sabe se encuentra a escasos centímetros, de qué color es, de qué forma, si está vivo o no, si puede emitir sonidos. La realidad parcial que lo constituye para él lo es todo y en base a eso debe poder interactuar con dicha realidad, aunque existan fenómenos que lo superen, por ejemplo, si el detecta la proximidad de un objeto y ese objeto desaparece, para el robot simplemente habrá un cambio de valor, quizás de un `10cm` a `100cm` que es su máximo, pero si había un objeto detrás de él, el cambio será de `10cm` quizás a `30cm` y lo podría interpretar mal, como si el objeto se estuviera alejando.

Los sensores, nos van a permitir establecer programas que reaccionen a un contexto, por ejemplo, prender automáticamente la luz cuando el sensor de intensidad de luz este por debajo de un umbral y apagar la luz cuando el sensor este por arriba de otro umbral. Esto nos va a permitir crear un entorno "inteligente", ya que por ejemplo, si colocamos sensores de luz dentro y fuera de una casa, podremos automatizar la apertura de persianas para que entre más claridad a la casa, el cierre automático en caso que sea de tarde o noche, podremos prender automáticamente los focos y quizás hacer sonar la alarma cuando sea de día. Cada uno de los sensores tiene casi infinitas capacidades de automatización, desde regar las plantas del jardín automáticamente cuando la humedad sea escasa, tapar un cultivo cuando la luz sea intensa, calentar o enfriar la casa para mantener un nivel estable de temperatura, abrir la puerta, prender las luces o sonar una alarma en caso de detectar movimiento o cerrar el ducto principal de gas en caso de detectar una fuga. Más aún, se pueden crear entornos inteligentes para alertar fuentes de emisión de contaminantes, alertar a la población en caso de un sismo, establecer cuales son los puntos en una ciudad con mayor cantidad de lluvia, para quizás establecer un centro de recolección de agua pluvial.

## Sensor de Luz (Foto-Resistor)

El sensor de luz consiste en un foto-resistor que es algo así como una resistencia que puede disminuir el voltaje que pasa a través de ella, dependiendo de la cantidad de luz que capta la cabeza.

Para que un foto-resistor funcione necesitamos pasar voltaje de un lado `[+]` y del otro lado conectarlo a un pin de entrada del `GPIO` al mismo tiempo que se conecta a un capacitor de `1uF` (el capacitor se conecta en salia a la tierra `[-]`).

Un esquema textual de la conexión es:

~~~txt
# FR - Foto-Resistor
# CP - Capacitor (1uF)
# [+] - 3.3v

[+] -> in:FR
FR:out |-> pin:GPIO
FR:out |-> in:CP
CP:out -> [-]
~~~

El programa de `python` encargado de leer el sensor deberá leer los datos de entrada del foto-resistor, para lograr esto se debe enviar un pulso de salida bajo (`LOW`) durante `0.1` segundos, luego se deberá esperar un pulso bajo (cuando se vacía el capacitor) como entrada, la acumulación en el tiempo de vaciado del capacitor indicará un valor asociado a la intesidad de luz y ese será nuestro valor del sensor.

El siguiente código muestra cómo leer un sensor de luz (foto-resistor) en el `PIN-18 BCM`:

~~~py
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM) # Indicamos que el modo de numeracion de pines sera BCM
GPIO.cleanup() # limpiamos GPIO

def LeerSensorLuz(pin):
    r = 0 # Acumula valores hasta el vaciado
    
    # Enviamos un pulso bajo (el foto-resistor acumula el capacitor)
    GPIO.setup(pin, GPIO.OUT) # Establece el pin en modo salida
    GPIO.output(pin, GPIO.LOW) # Envia un pulso bajo
    time.sleep(0.1) # Detiene el programa por 0.1 segundos

    GPIO.setup(pin, GPIO.IN) # Establece el pin en modo entrada

    # Leemos el pin hasta que la lectura sea un `LOW`
    # esto significa que el capacitor se ha vaciado
    while GPIO.input(pin) == GPIO.LOW:
        r += 1 # incrementamos el valor de lectura mientras el capacitor se vacia

    return r # Devolvemos cuantas acumulaciones hubo, esto estara variando
    # dependiendo de la intensidad que perciba el foto-resistor

inciarSensorLuz(18)

# Leemos infinitamente el sensor de luz en el `PIN-18 BCM`
while True:                                    
    print("Sensor de luz: {}".format(LeerSensorLuz(18)))
~~~

### Ejercicios

* Guarda el valor del sensor en una variable
* Guarda el valor mínimo del sensor y el máximo
* Imprime el porcentaje del sensor respecto a su mínimo y máximo (Sólo si el mínimo es distinto del máximo)

## Sensor de distancia (Ultrasónico)

Uno de los métodos más creativos para medir la distancia que existe a un objeto consiste en lanzar un pulso ultrasónico, cuando este pulso rebota en el objeto genera un pulso similar pero distorcionado que puede ser escuchado de regreso, el nivel de distorsión indicará cual es la distancia entre el objeto y el dispositivo que emite y escucha la señal que rebota. Este mecanismo por más ficticio que parezca es implementado en la naturaleza por los murciélagos para tener una visión dentro de las cuevas profundas donde habitan, y se desarrolló seguramente porque dichas cuevas eran seguras para protegerse ahí de depredadores.

El sensor ultrasónico materializa estos conceptos en un dispositivo capaz de generar un pulso ultasónico y escuchar el rebote, para así medir la distancia entre el sensor y un objeto. La precisión y límites del sensor serán especificados por cada fabricante, pero los más económicos mediras poco más que algunas decenas de centímetros.

El sensor ultrasónico consta de `4` pines nombrados como `GND`, `ECHO`, `TRIG`, `VCC` de los cuales `TRIG` es el encargado de disparar el pulso ultrasónico y `ECHO` el encargado de escuchar el rebote.

El esquema textual para conectar el sensor a la `Raspberry Pi` es el siguiente:

~~~txt
# UL - Ultrasónico
# R1k - Resistencia 1k ohms
# R2k - Resistencia 2k ohms
# [+] - 5v

UL:vcc -> [+]
UL:trig -> pin-trig:GPIO
UL:echo -> pin-echo:GPIO -> R1k
UL:gnd -> R2k
R1k + R2k -> [-]
~~~

El programa de `python` encargado de leer el sensor deberá asegurarse que `TRIG` está en `LOW`, esto podría demorar más la primera vez, quizás un par de segundos. Deberemos activar `TRIG` durante `0.00001` segundos (`10uS`) para después desactivarlo nuevamente. Una vez emitido el pulso ultrasónico, deberemos leer dicho pulso mediante `ECHO`, midiendo la diferencia de los segundos desde que el pulso es `bajo` hasta que el pulso es `alto`, la duración del pulso (dicha diferencia) nos dirá cuál es la distancia del objeto por la ecuación `V = D / T` que indica la relación entre velocidad, distancia y tiempo. La velocidad del sonido es `343` metros por segundo, y el tiempo será la duración del pulso, sin embargo, la distancia se tiene que contar dos veces ya que es la distancia de ida más la de vuelta, por lo que tenemos que `34300 = (2 * d) / T` donde `T` es la duración que leímos del pulso, por lo tanto `d = 17150 * T`, la cual estará en unidades de centímetros (observa que se coloca `34300` en lugar de `343` que es la velocidad del sonido en centímetros por segundo).

El siguiente código muestra cómo leer un sensor de distancia (ultrasónico) en los pines `TRIG: PIN-23 BCM`, `ECHO: PIN-24 BCM`:

~~~py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Indicamos que el modo de numeracion de pines sera BCM
GPIO.cleanup() # limpiamos GPIO

def iniciarSensorDistancia(pin_trig, pin_echo):
    GPIO.setup(pin_trig, GPIO.OUT) # Ajustamos TRIG como salida
    GPIO.setup(pin_echo, GPIO.IN) # Ajustamos ECHO como entrada

    # Nos aseguramos que TRIG este apagado
    GPIO.output(pin_trig, GPIO.LOW)
    time.sleep(2)

def LeerSensorDistancia(pin_trig, pin_echo):
    # Prendemos TRIG durante 10uS y luego lo apagamos
    GPIO.output(pin_trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(pin_trig, GPIO.LOW)

    # Iniciamos la lectura del rebote
    while GPIO.input(pin_echo) == GPIO.LOW:
        pulse_start = time.time()

    # Finalizamos la lectura del rebote
    while GPIO.input(pin_echo) == GPIO.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start # Duracion del pulso de rebote

    distance = pulse_duration * 17150 # distancia calculada en `cm`

    return distance

inicarSensorDistancia(23, 24)

while True:
    print("Distancia: {:.2f} cm".format(LeerSensorDistancia(23, 24)))
~~~

### Ejercicios

* Guardar la distancia leída en una variable
* Almacenar las últimas 20 distancias leídas
* Cada 20 lecturas, borrar la pantalla en la terminal
* Después de borrar la terminal imprimir para cada una de las 20 lecturas un guión por cada centímetro leído en la distancia, ejemplo:

~~~txt
| ----
| ---------
| ---------------
| ------
...
~~~

## Sensor de Humedad y Temperatura (DHT11)

El sensor de Humedad+Temperatura consiste en un dispositivo que es capaz de leer el porcentaje de Humedad Relativa en el aire (RH - https://en.wikipedia.org/wiki/Relative_humidity) que indica un porcentaje de humedad respecto al agua (Aire vs Agua) y la temperatura en un rango de `0º` a `50º`.

El sensor `DHT11` es un sensor digital que codifica la lectura de los datos de humedad y temperatura en un dato binario (8+8 bits para humedad, 8+8 bits para temperatura y 8 bits de paridad para checar si los datos no están corruptos, en total 40 bits). Generalmente el sensor cuenta con tres pines que son `GND`, `DATA`, `VCC` donde `DATA` envía el paquete de bits con la lectura de humedad y temperatura, hay que tomar en cuenta que leer los datos en intervalos menores a 5 segundos podría arrojar datos menos precisos.

El esquema textual para conectar el sensor sería el siguiente:

~~~txt
# HT - DHT11
# [+] - 3.3v ~ 5v

HT:gnd -> [-]
HT:data -> pin-data:GPIO
HT:vcc -> [+]
~~~

El programa de `python` encargado de leer el sensor utilizará el módulo `dht11.py` creada por `github:szazo` y disponible en github:

> dht11.py (https://github.com/szazo/DHT11_Python/blob/master/dht11.py)

~~~py
import time
import RPi


class DHT11Result:
    'DHT11 sensor result returned by DHT11.read() method'

    ERR_NO_ERROR = 0
    ERR_MISSING_DATA = 1
    ERR_CRC = 2

    error_code = ERR_NO_ERROR
    temperature = -1
    humidity = -1

    def __init__(self, error_code, temperature, humidity):
        self.error_code = error_code
        self.temperature = temperature
        self.humidity = humidity

    def is_valid(self):
        return self.error_code == DHT11Result.ERR_NO_ERROR


class DHT11:
    'DHT11 sensor reader class for Raspberry'

    __pin = 0

    def __init__(self, pin):
        self.__pin = pin

    def read(self):
        RPi.GPIO.setup(self.__pin, RPi.GPIO.OUT)

        # send initial high
        self.__send_and_sleep(RPi.GPIO.HIGH, 0.05)

        # pull down to low
        self.__send_and_sleep(RPi.GPIO.LOW, 0.02)

        # change to input using pull up
        RPi.GPIO.setup(self.__pin, RPi.GPIO.IN, RPi.GPIO.PUD_UP)

        # collect data into an array
        data = self.__collect_input()

        # parse lengths of all data pull up periods
        pull_up_lengths = self.__parse_data_pull_up_lengths(data)

        # if bit count mismatch, return error (4 byte data + 1 byte checksum)
        if len(pull_up_lengths) != 40:
            return DHT11Result(DHT11Result.ERR_MISSING_DATA, 0, 0)

        # calculate bits from lengths of the pull up periods
        bits = self.__calculate_bits(pull_up_lengths)

        # we have the bits, calculate bytes
        the_bytes = self.__bits_to_bytes(bits)

        # calculate checksum and check
        checksum = self.__calculate_checksum(the_bytes)
        if the_bytes[4] != checksum:
            return DHT11Result(DHT11Result.ERR_CRC, 0, 0)

        # ok, we have valid data, return it
        return DHT11Result(DHT11Result.ERR_NO_ERROR, the_bytes[2], the_bytes[0])

    def __send_and_sleep(self, output, sleep):
        RPi.GPIO.output(self.__pin, output)
        time.sleep(sleep)

    def __collect_input(self):
        # collect the data while unchanged found
        unchanged_count = 0

        # this is used to determine where is the end of the data
        max_unchanged_count = 100

        last = -1
        data = []
        while True:
            current = RPi.GPIO.input(self.__pin)
            data.append(current)
            if last != current:
                unchanged_count = 0
                last = current
            else:
                unchanged_count += 1
                if unchanged_count > max_unchanged_count:
                    break

        return data

    def __parse_data_pull_up_lengths(self, data):
        STATE_INIT_PULL_DOWN = 1
        STATE_INIT_PULL_UP = 2
        STATE_DATA_FIRST_PULL_DOWN = 3
        STATE_DATA_PULL_UP = 4
        STATE_DATA_PULL_DOWN = 5

        state = STATE_INIT_PULL_DOWN

        lengths = [] # will contain the lengths of data pull up periods
        current_length = 0 # will contain the length of the previous period

        for i in range(len(data)):

            current = data[i]
            current_length += 1

            if state == STATE_INIT_PULL_DOWN:
                if current == RPi.GPIO.LOW:
                    # ok, we got the initial pull down
                    state = STATE_INIT_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_INIT_PULL_UP:
                if current == RPi.GPIO.HIGH:
                    # ok, we got the initial pull up
                    state = STATE_DATA_FIRST_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_FIRST_PULL_DOWN:
                if current == RPi.GPIO.LOW:
                    # we have the initial pull down, the next will be the data pull up
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_UP:
                if current == RPi.GPIO.HIGH:
                    # data pulled up, the length of this pull up will determine whether it is 0 or 1
                    current_length = 0
                    state = STATE_DATA_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_DOWN:
                if current == RPi.GPIO.LOW:
                    # pulled down, we store the length of the previous pull up period
                    lengths.append(current_length)
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue

        return lengths

    def __calculate_bits(self, pull_up_lengths):
        # find shortest and longest period
        shortest_pull_up = 1000
        longest_pull_up = 0

        for i in range(0, len(pull_up_lengths)):
            length = pull_up_lengths[i]
            if length < shortest_pull_up:
                shortest_pull_up = length
            if length > longest_pull_up:
                longest_pull_up = length

        # use the halfway to determine whether the period it is long or short
        halfway = shortest_pull_up + (longest_pull_up - shortest_pull_up) / 2
        bits = []

        for i in range(0, len(pull_up_lengths)):
            bit = False
            if pull_up_lengths[i] > halfway:
                bit = True
            bits.append(bit)

        return bits

    def __bits_to_bytes(self, bits):
        the_bytes = []
        byte = 0

        for i in range(0, len(bits)):
            byte = byte << 1
            if (bits[i]):
                byte = byte | 1
            else:
                byte = byte | 0
            if ((i + 1) % 8 == 0):
                the_bytes.append(byte)
                byte = 0

        return the_bytes

    def __calculate_checksum(self, the_bytes):
        return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255
~~~

El siguiente código muestra cómo leer un sensor de humedad+temperatura (DHT11) en el pin `DATA: PIN-14 BCM`:

~~~py
import RPi.GPIO as GPIO
from dht11 import DHT11
import time
import datetime

GPIO.setmode(GPIO.BCM) # Indicamos que el modo de numeracion de pines sera BCM
GPIO.cleanup() # limpiamos GPIO

sensor = DHT11(pin=14) # Creamos una instancia de la clase DHT11

while True:
    result = sensor.read() # Leemos el sensor y obtenemos un objeto con los resultados
    if result.is_valid(): # Si el resultado es valido imprimimos los datos
        print("Ultima lectura valida: {}".format(datetime.datetime.now()))
        print("Temeperatura: {:.2f} C".format(result.temperature))
        print("Humedad: {:.2f}%".format(result.humidity))
    time.sleep(1) # Esperamos 1 segundo entre cada lectura
~~~

### Ejecicios

* Guardar los valores de la humedad y temperatura en variables
* Si la temperatura es mayor a 20ºC imprimir: `"APAGAR CALEFACTOR + PRENDER CLIMA"`
* Si la temperatura es menor a 10ºC imprimir: `"APAGAR CLIMA + PRENDER CALEFACTOR"`
* Si la humedad es menor a 30% imprimir: `"PRENDER RIEGO"`
* Si la humedad es mayor a 80% imprimir: `"APAGAR RIEGO"`
* Guardar las lecturas de humedad y temperatura en un archivo

## Retos

* Crear un servidor web que defina las rutas: `/sensor/X`, `/sensor/X/log` y `/sensor/X/grafica` cómo se trabajó en la **Sesión 1** y poder ver en tiempo real la gráfica y valores de cada sensor.

* Conectar al menos dos sensores y leerlos al mismo tiempo mediante hilos.