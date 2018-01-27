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