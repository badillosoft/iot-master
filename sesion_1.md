# Sesión 1 - Python y los Servicios Web

Por Alan Badillo Salas (badillo.soft@hotmail.com)

## Introducción

Python es un lenguaje de programación muy versátil, sencillo, potente y elegante, lo que lo convierte en una excelente opción para programar. Este lenguaje ha sido implementado nativamente en sistemas operativos basados en Unix, de tal forma que al acceder a cualquier terminal podemos teclear el comando `python --version` para obtener la versión instalada de python, que generalmente será la versión `2.7.x`.

Todo lenguaje de programación posee elementos que definen la sintaxis y estructura general del código para poder ser interpretado, sin embargo, también existen paradigmas de programación que indican un modo global de cómo deberían ser escritos los programas.

## Introducción a la programación

Para aquellos que aún no se han iniciado en la programación, deberán comprender los elementos fundamentales de como escribir programas. Un programa es un conjunto de instrucciones que recibe la computadora e interpreta para realizar operaciones agrupadas a veces en tareas.

Los elementos de cualquier lenguaje de programación son:

* __Variables__: Nos permiten almacenar datos en la memoria temporal, de tal forma que podemos utilizarlos despúes para completar otras operaciones. Las variables funcionan como cajas de almacenamiento distinguidas entre sí por un nombre de variable, el cuál generalmente es una palabra simple o un conjunto de palabras agrupadas, por ejemplo: `personas`, `nombreEstudiante`, `mi_variable`, etc.

* __Estructuras de control__: Las estructuras de control (de flujo) nos permiten establecer mecanismos para ejecutar bloques de código dependiendo si una condición se cumple, o incluso si el bloque debe repetirse determinadas veces o indeterminadas veces. Las estructuras de control más comunes son las condiciones (`if-else`) y los ciclos (`for | while`).

* __Funciones__: Cuando una tarea queda resuelta, es decir, cuándo logramos implementar un algoritmo que resuelve una tarea específica, generalmente dicha tarea puede ser abstraída en un bloque funcional, dicho bloque estará compuesto de un conjunto de instrucciones y estructuras de control. Para poder generalizar dicha tarea, identificaremos las variables que puedan ser sustituidos por otros valores, de tal forma que la tarea se configure por un conjunto de parámetros para funcionar. Una función define un bloque de código que puede recibir parámetros como entrada con diversos valores y ejecuta una tarea específica. Piense por ejemplo la tarea de abrir un archivo, dicha tarea puede ser realizada para un sin número de nombres de archivos, en tal caso, el nombre del archivo será el parámetro de la función.

* __Módulos__: Cuando queremos exportar un conjunto de funciones (`tareas`) para formar una biblioteca de módulo, generalmente contruimos módulos funcionales, los cuales le permiten al programador, definir en el módulo todas las tareas que ya funcionan y están programadas, para en otro programa importar dicho módulo y utilizar las funciones reduciendo el código y dejándolo elegante.

* __Operaciones__: Todo lenguaje también es una potente calculadora de expresiones, podemos hacer sumas, restas, multiplicaciones, divisiones, comparaciones de desigualdad y de igualdad, operaciones lógicas de conjunción, disyunción, negación y algunas cosas más.

* __Colecciones__: La potencia de los lenguajes de programación modernos reside en su facilidad para operar colecciones complejas como listas, matrices y diccionarios. El dominar las colecciones de un lenguaje nos permitirá almacenar y procesar información compleja y realizar programas más sofisticados y eficientes.

## Introducción a Python

Python es un lenguaje de programación moderno, basado en código interpretado y fuertemente tipado, lo que significa, que nuestro programa será procesado línea por línea mediante un intérprete, el cual realizará todas las operaciones y tareas solicitadas en tiempo real. Python es fuertemente tipado, lo que significa que no es necesario establecer el tipo de dato que será almacenado en sus variables ya que lo interpretará automáticamente, además Python nos permite definir variables en cualquier momento sin tener que hacer una declaración de uso.

> El siguiente programa crea dos variables de tipo entero e imprime la suma de ellos:

~~~py
a = 123
b = 456

print(a + b)
~~~

Observa que no es necesario declarar el uso previo de `a` o `b` ni su tipo de dato, también imprimimos directamente el resultado de la suma `a + b`.

En python podemos crear condiciones que determinen si un bloque será ejecutado, o si por el contrario, de no cumplirse ejecutará otro bloque.

> El siguiente programa crea dos variables e imprime el valor de el mayor de ellas

~~~py
a = 123
b = 456

if a > b:
    print(a)
else:
    print(b)
~~~

Como puede deducir, python ejecutará el bloque `: print(a)` sólo si se cumple la condición generada por la comparación `a > b` y en caso de no cumplirse evaluará el bloque `: print(b)`.

El bloque `else` es opcional y debe ponerse después de cualquier anidación `if` o `if-elif`.

> El siguiente programa imprime el rango de edad correspondiente a una variable que almacena un entero referente a una edad

~~~py
edad = 34

if a <= 12:
    print("infante")
elif a <= 20:
    print("adolescente")
elif a <= 30:
    print("joven")
else:
    print("adulto")
~~~

Intuye que python evaluará la primer condición `a <= 12` y de cumplirse ejecutará el bloque `: print("infante")`, de no cumplirse evaluará la condición `a <= 20` y ejecutará su bloque asociado, si ningún bloque se cumple se puede definir un `else` que sea ejecutado en cualquier otro caso (`else` y `elif` son opcionales, pero sólo puede haber un `else` y debe ser declarado al final de la cascada de condiciones).

Para repetir un bloque de código podemos utilizar la estructura `for` la cuál nos permite recorrer un `iterable` que puede ser un `rango` o una `colección`. Los rangos pueden ser construidos de distintas formas: `range(n)` que itera los números enteros de `0` a `n - 1`, `range(a, b)` que itera los números enteros de `a` hasta `b - 1` y `range(a, b, s)` que itera los números enteros de `a` a `b - 1` con saltos de `s`.

> El siguiente programa imprime los números del `1` al `100`

~~~py
for i in range(1, 101):
    print(i)
~~~

Observa que los rangos no tocan el último número (`101`) y retienen el valor del iterador en la variable `i` (se puede llamar de otra forma). En cada iteración `i` tendrá el valor cedido por `range`, por ejemplo, en la primer iteración tendrá el valor de `1` y en la última el valor de `100`. En cada iteración ejecutará el bloque `: print(i)` imprimiendo el valor actual de `i`.

Presta atención que en todos los códigos anteriores los bloques declarados como `: ···` poseen una identación, es decir, que el código que pertenece al bloque es especifícado por espacios o tabuladores que separan el código a la derecha. Esto es estrictamente necesario para indicar que las instrucciones pertenecen a ese bloque, pero ten cuidado con no colocar código mal indentado, pro ejemplo:

~~~py
s = 0

for i in range(1, 101):
    print(i)
s = s + i
~~~

El código anterior va a imprimir los números del `1` al `100` y cuando haya acabado ejecutará la línea `s = s + i`, para este momento `i` no pertenece al bloque y su valor podría no ser ninguno esperado y `s` podría contener un valor extraño. Lo correcto sería:

~~~py
s = 0

for i in range(1, 101):
    print(i)
    s = s + i

print("La suma de los numeros del 1 al 100 es: %d" %s)
~~~

Donde el valor de `s` será reemplazado en la cadena donde indica `%d`.

## Tópicos de Python

Ahora pasemos a hablar de algunos temas más avanzados del lenguaje python. Comenzaremos por revisar el funcionamiento de las colecciones.

Una colección es un conjunto de datos estructurados de dos formas en python: `listas` y `diccionarios` principalmente, aunque también existen las `tuplas` que vendrían a ser listas estáticas.

Las `listas` son arreglos de datos retenidos en una misma variable e indexados comenzando en el índice `0`. Una lista tiene la propiedad de crecer o decrecer y posee métodos para seguir insertando elementos y también para quitar elementos.

> Ejemplo de una lista

~~~py
A = [1, 2, 5, 8, 9]
~~~

Las listas pueden ser creadas fácilmente por medio de los `[]` y los elementos separados por comas, una lista puede almacenar cualquier cosa que quepa en una variable, incluso una función.

Las listas poseen principalmente los métodos:

* __[].append(*x*)__: Agrega el elemento `x` a la lista
* __[].insert(*i*, *x*)__: Agrega el elemento `x` a la lista en el índice `i`
* __[].remove(*x*)__: Quita el primer elemento `x` que se encuentre en la lista, pero si no encuentra ninguno causa error
* __[].pop(*i*)__: Quita el elemento de la lista con índice `i` y si no existe causa error. En caso de que `i` sea `-1` eliminará el último, `-2` el penúltimo y así

> El siguiente programa agrega y quita elementos

~~~py
x = [6, 8, 9, 8]

x.append(4) # [6, 8, 9, 8, 4]
x.remove(8) # [6, 9, 8, 4]
x.insert(2, 5) # [6, 9, 5, 8, 4]
x.pop(-3) # [6, 9, 8, 4]

x[0] = 1 # [1, 9, 8, 4]

print(x[3]) # 4
~~~

Los diccionarios funcionan como las listas con la diferencia de almacenar datos en tablas `clave-valor` (`hash`), es decir, que un diccionario es una colección en la que se almacena un valor en una `clave` dada y no en un índice, el orden de los elementos aquí no importa.

> Ejemplo de un diccionario

~~~py
p = {
    "nombre": "Alan",
    "x": 123,
    "y": 456,
    "maestro": True
}

p["nombre"] = "Alan Badillo" # reemplaza el valor almacenado en la clave nombre
p["pais"] = "MX" # agrega la clave "pais" con el valor almacenado "MX"

print(p["x"]) # 123
print(p["z"]) # error la clave no existe
~~~

Otro tema importante son las funciones, estás nos permiten definir tareas completas, encapsularlas y generalizar sus parámetros variables.

Una función se define mediante `def nombre(parametros): bloque`, por ejemplo, la siguiente función devuelve el valor máximo entre dos valores recibidos

~~~py
def mayor(a, b):
    if a > b:
        return a
    else:
        return b

print(mayor(1, 5)) # 5
print(mayor(5, 1)) # 5
print(mayor(100, 99)) # 100
~~~

Las funciones son útiles para dejar implementados algoritmos complejos y poder utilizarlos facilmente, por ejemplo, el siguiente código ordena una lista de números de forma ascendente:

~~~py
def ordenar(A):
    # Creamos un arreglo vacío
    B = []

    # Mientras <el número de elementos de A> sea mayor a cero
    while len(A) > 0:
        # Obtener el valor mínimo de A
        x = min(A)
        # Quitar el valor mínimo de A
        A.remove(x)
        # Agregar el valor mínimo de A a B
        B.append(x)

    return B

print(ordenar([1, 4, 3, 5, 0, 2])) # [0, 1, 2, 3, 4, 5]
~~~

Estos son los fundamentos de Python, aún faltan muchas cosas por aprender, pero está guía debió haberte dado una noción general de python y el cómo opera.

## Servicios Web

Un servicio web se refiere a operaciones que serán realizadas por un programa remoto disponible en nuestra red, en este caso nuestra Raspberry funcionará como un servidor listo para realizar operaciones y devolvernos los resultados, por ejemplo, el valor de los sensores leídos, el resultado de aplicar un actuador, o incluso el resultado de realizar tareas complejas como mandar un email informando que se detectó actividad en nuestra casa informado por el sensor de movimiento haciendo sonar la alarma.

Para crear un servicio web en python, deberemos utilizar `Flask` el cual es un pequeño framework orientado a montar un servidor de recursos en python. El siguiente código muestra como levantar un servidor en el host y puerto por defecto `http://localhost:5000/`.

~~~py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Flask"

app.run()
~~~

Para poder ejecutar el programa deberemos instalar el módulo externo `flask` mediante `pip install flask`. Luego si ejecutamos el código podremos abrir un navegador web en la ruta http://localhost:5000/ y obtener una misteriosa respuesta.

En una red local podremos incluso acceder al servidor que estará generando la Raspberry desde nuestra computadora o nuestro teléfono celular :D

Algo interesante de Flask es la posibilidad de utilizar plantillas `HTML` para enviarlas al usuario, estas plantillas serán archivos html alojados en la carpeta `/templates` y utilizaremos `render_template` para enviar dicho código html. El siguiente programa monta un servidor flask y envía la plantilla `hello.html`

> /server.py

~~~py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("hello.html")

app.run()
~~~

> /templates/hello.html

~~~html
<h1>Hola Flask :D</html>
~~~

El resultado será que cada que el usuario ingrese al recurso `/` verá el archivo html rendereado por flask.

Python y Flask además tienen la capacidad de generar gráficas mediante el módulo `matplotlib` las cuales pueden ser enviadas como imágenes `PNG` por nuestro servidor, de tal forma que le podemos mostrar al usuario gráficas en tiempo real de cómo se están comportando nuestro sensores.

> El siguiente programa genera una imágen en la ruta `/imagen`

~~~py
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
    
    # Dibujamos la gráfica
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
~~~

## Hilos

En Python es importante realizar tareas en hilos para no detener el flujo del programa y la forma más sencilla es la siguiente:

~~~py
import threading
import time

def task_1():
    for i in range(10):
        print("TASK 1 %d" % i)
        time.sleep(1)

def task_2():
    for i in range(5):
        print("TASK 2 %d" % i)
        time.sleep(2)

threading.Thread(target=task_1).start()
threading.Thread(target=task_2).start()

print("Tareas iniciadas...")
~~~

El programa anterior define dos funciones que realizan tareas similares, la primer función `task_1` imprime números del `0` al `9` cada segundo, y `task` dos imprime números del `0` al `4` cada dos segundos, ambas tareas son encapsuladas en hilos y ejecutadas en `paralelo*`. Así podemos ejecutar dos o más tareas distintas sin bloquear el flujo.

## Simular sensores

Como en la primera sesión no utilizaremos las raspberry, veremos como simular algunos sensores para poder hacer un poco de control automático y generar algunos reportes.

Para simular un sensor podemos generar valores aleatorios cada determinado tiempo en un hilo, por ejemplo:

~~~py
import threading
import time
import random

distancia = -1

def leer_distancia():
    global distancia
    while True:
        distancia = random.uniform(10, 100)
        print("la distancia es: {} cm".format(distancia))
        time.sleep(1)

print("Tareas iniciadas...")
threading.Thread(target=leer_distancia).start()
~~~

Ahora podemos proveer un servicio web para ver la distancia:

~~~py
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
~~~

> Inicia http://localhost:5000/sensor/distancia

Ahora podemos almacenar las últimas `100` lecturas

~~~py
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
~~~

> Inicia http://localhost:5000/sensor/distancia/log

Ahora podemos generar una imagen en tiempo real de las últimas 100 lecturas de nuestro sensor simulado:

~~~py
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
~~~

> Inicia http://localhost:5000/sensor/distancia/grafica

Finalmente podemos crear un servidor y una página que le muestre al usuario los valores del sensor y su gráfica cada segundo.

> /simulador.5.py

~~~py
# -*- coding: utf-8 -*-
from flask import Flask, make_response, render_template
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

@app.route("/")
def home():
    return render_template("home.html")

print("iniciando servidor...")
app.run()
~~~

> /templates/home.html

~~~html
<h1>Sensor Distancia</h1>

<p id="valor"></p>

<img src="/sensor/distancia/grafica">

<ul id="registro"></ul>

<script>
    function obtener_distancias() {
        return new Promise((resolve, reject) => {
            const req = new XMLHttpRequest();
            req.open('GET', '/sensor/distancia/log', true);
            
            req.onreadystatechange = () => {
                if (req.readyState == 4) {
                    if(req.status == 200) {
                        const data = JSON.parse(req.responseText);
                        resolve(data);
                        return;
                    }
                    
                    reject("Error al cargar los datos");
                }
            };
            
            req.send(null);
        });
    }

    window.onload = () => {
        const img = document.querySelector("img");
        const valor = document.getElementById("valor");
        const registro = document.getElementById("registro");

        setInterval(() => {
            img.src = `/sensor/distancia/grafica?seed=${new Date()}`;

            obtener_distancias().then(distancias => {
                valor.innerHTML = `${distancias[distancias.length - 1]}`;
                registro.innerHTML = distancias.map(d => {
                    return `<li>${d}</li>`;
                }).join("");
            }).catch(err => {
                valor.innerHTML = err;
                registro.innerHTML = "";
            });
        }, 1000);
    };
</script>
~~~