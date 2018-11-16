# -*- coding: utf-8 -*-
#!/usr/bin/python

#Script para enviar datos al SmartPhone

import RPi.GPIO as GPIO
import sys
import signal
import Adafruit_DHT
import socket,time
from time import gmtime, strftime

GPIO.setmode(GPIO.BOARD)
pinTrigger = 22
pinEcho = 12

def close(signal, frame):
	print("\nTurning off ultrasonic distance detection...\n")
	GPIO.cleanup() 
	sys.exit(0)

signal.signal(signal.SIGINT, close)

GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

def readDistance():
    GPIO.output(pinTrigger, True)
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)
    startTime = time.time()
    stopTime = time.time()

    # save start time
    while 0 == GPIO.input(pinEcho):
    	startTime = time.time()

    # save time of arrival
    while 1 == GPIO.input(pinEcho):
        stopTime = time.time()

    TimeElapsed = stopTime - startTime
    distance = (TimeElapsed * 34300) / 2
    
    #d = '%.2f'%(distance)
    #distance=distance/100
    #print("Distancia: %.2f mts." % distance)
    return distance-5


while True:
	localtime = strftime("%H:%M:%S", gmtime())

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		s.connect(("192.168.1.66", 8888)) #IP Smartphone
		distancia = readDistance()
		humedad,temperatura = Adafruit_DHT.read(Adafruit_DHT.DHT11,21)
		#print("Temperatura={0:0.1f}°C Humedad={1:0.1f}%".format(temperatura,humedad))
		cadena=str(temperatura)+","+str(humedad)+","+str('%.2f'%(distancia))
		s.send(bytes(cadena+"\r\n",'UTF-8'))
		print(">> ",localtime," Mensaje Enviado...", cadena)
		s.close()
		time.sleep(0.5)
	except KeyboardInterrupt:
                print("Bye bye :)")
                sys.exit()

	except Exception as e:
		print(">> ",localtime," Primero inicie la interfaz de Endurance... ",e)
		time.sleep(0.5)


