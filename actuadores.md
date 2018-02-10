# Actuadores

Por Alan Badillo Salas (badillo.soft@hotmail.com)

## Introducción

Un actuador es un dispositivo capaz de recibir señales para producir respuestas mécanicas e interacturar con el entorno. Un actuador primitivo consiste en los flagelos que usan células y bacterias para poder moverse, dicho flagelo recibe señales mediante proteinas y la variación de estas señales provoca que se mueva de formas distintas.

## Motor a pasos

Un motor a pasos consiste en 4 fases de pulsos para completar un paso, cuando las 4 fases son establecidas se produce un paso y el cúmulo de 512 pasos forman una vuelta completa de la hélice de motor. Este actuador nos permite controlar con precisión las vueltas que da un motor.

El motor a pasos `28BYJ-48` cuenta con un módulo de control `ULN2003`. El controlador funciona en 4 fases nombradas `A B C D`. Las cuales pueden activarse individualmente, en pares o medios pasos. Los pines están numerados `IN1 IN2 IN3 IN4`.

> stepper.py

~~~py
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class StepperMotor:
	def __init__(self, in1, in2, in3, in4):
		self.p1 = in1
		self.p2 = in2
		self.p3 = in3
		self.p4 = in4
		self.delay = 0.004
		GPIO.setup(in1, GPIO.OUT)
		GPIO.setup(in2, GPIO.OUT)
		GPIO.setup(in3, GPIO.OUT)
		GPIO.setup(in4, GPIO.OUT)
	def stepForward(self):
		GPIO.output(self.p1, True)
		GPIO.output(self.p2, True)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, False)
		time.sleep(self.delay)
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, True)
		GPIO.output(self.p3, True)
		GPIO.output(self.p4, False)
		time.sleep(self.delay)
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, True)
		GPIO.output(self.p4, True)
		time.sleep(self.delay)
		GPIO.output(self.p1, True)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, True)
		time.sleep(self.delay)
	def stepBackward(self):
		GPIO.output(self.p1, True)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, True)
		time.sleep(self.delay)
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, True)
		GPIO.output(self.p4, True)
		time.sleep(self.delay)
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, True)
		GPIO.output(self.p3, True)
		GPIO.output(self.p4, False)
		time.sleep(self.delay)
		GPIO.output(self.p1, True)
		GPIO.output(self.p2, True)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, False)
		time.sleep(self.delay)
	def goForward(self, steps=1):
		for i in range(steps):
			self.stepForward()
		self.off()
	def goBackwards(self, steps=1):
		for i in range(steps):
			self.stepBackward()
		self.off()
	def off(self):
		GPIO.output(self.p1, False)
		GPIO.output(self.p2, False)
		GPIO.output(self.p3, False)
		GPIO.output(self.p4, False)
~~~