import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM) # Indicamos que el modo de numeracion de pines sera BCM
GPIO.cleanup() # limpiamos GPIO

def LeerSensorLuz(pin):
    r = 0 # Acumula valores hasta el vaciado
    
    # Enviamos un pulso bajo (el foto-resistor acumula el capacitor)
    GPIO.setup(pin, GPIO.OUT) # Establece el pin en modo salida
    GPIO.output(pin, GPIO.LOW) # Envia un pulso bajo
    time.sleep(0.1) # Detiene el programa por 0.1 segundos

    GPIO.setup(pin, GPIO.IN) # Establece el pin en modo entrada

    # Leemos el pin hasta que la lectura sea un `LOW`
    # esto significa que el capacitor se ha vaciado
    while GPIO.input(pin) == GPIO.LOW:
        r += 1 # incrementamos el valor de lectura mientras el capacitor se vacia
        if r >= 2000:
            break

    return r # Devolvemos cuantas acumulaciones hubo, esto estara variando
    # dependiendo de la intensidad que perciba el foto-resistor

inciarSensorLuz(18)

# Leemos infinitamente el sensor de luz en el `PIN-18 BCM`
while True:                                    
    print("Sensor de luz: {}".format(LeerSensorLuz(18)))
