# -*- encoding: utf-8 -*-
#Script para enviar ordenes al robot
from socket import *
import sys
import time
import RPi.GPIO as GPIO
import os

print ('\n\n¯`·.¸¸.·´¯`·.¸¸.-> [ Servidor virtual Endurance by Oscar Alemán ] <-.¸¸.·´¯`·.¸¸.·´¯')
print ('\n\nEscuchando Peticiones...')

GPIO.setwarnings(False)

sleeptime=1

MI_pin_avanzar=13
MI_pin_retroceder=15

MD_pin_avanzar=16
MD_pin_retroceder=18

#Usamos los pines fisicos del Raspberry
GPIO.setmode(GPIO.BOARD)

#Inicializamos motores
GPIO.setup(MI_pin_avanzar, GPIO.OUT)
GPIO.setup(MI_pin_retroceder, GPIO.OUT)

GPIO.setup(MD_pin_avanzar, GPIO.OUT)
GPIO.setup(MD_pin_retroceder, GPIO.OUT)

def avanzar(x):
    GPIO.output(MI_pin_avanzar, GPIO.HIGH)
    GPIO.output(MD_pin_avanzar, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(MI_pin_avanzar, GPIO.LOW)
    GPIO.output(MD_pin_avanzar, GPIO.LOW)
    print ("\tEjecutado!")

def retroceder(x):
    GPIO.output(MI_pin_retroceder, GPIO.HIGH)
    GPIO.output(MD_pin_retroceder, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(MI_pin_retroceder, GPIO.LOW)
    GPIO.output(MD_pin_retroceder, GPIO.LOW)
    print ("\tEjecutado!")

def girarIzquierda(x):
	GPIO.output(MI_pin_retroceder, GPIO.HIGH)
	GPIO.output(MD_pin_avanzar, GPIO.HIGH)
	time.sleep(x)
	GPIO.output(MI_pin_retroceder, GPIO.LOW)
	GPIO.output(MD_pin_avanzar, GPIO.LOW)
	print ("\tEjecutado!")

def girarDerecha(x):
	GPIO.output(MD_pin_retroceder, GPIO.HIGH)
	GPIO.output(MI_pin_avanzar, GPIO.HIGH)
	time.sleep(x)
	GPIO.output(MD_pin_retroceder, GPIO.LOW)
	GPIO.output(MI_pin_avanzar, GPIO.LOW)
	print ("\tEjecutado")

peticiones = ['GO','BACK','LEFT','RIGHT','APAGAR','REINICIAR']
dominio = ''
puerto = 9999
servidor = (dominio,puerto)

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(servidor)
tcpSocket.listen(5)

while True:
	try:
		tcpClienteSocket,cliente = tcpSocket.accept()
		print ('\n>> Peticion recibida de la IP ',cliente[0])
		while True:
		        datos = ''
		        datos = tcpClienteSocket.recv(1024).decode()

		        if not datos:
		                break

		        if datos == peticiones[0]:
		        	avanzar(.5)

		        if datos == peticiones[1]:
		        	retroceder(.5)

		        if datos == peticiones[2]:
		            girarIzquierda(.1)

		        if datos == peticiones[3]:
		            girarDerecha(.1)
		            
		        if datos == peticiones[4]:
		            os-system('sudo shutdown -h now')
		            
		        if datos == peticiones[5]:
		            os.system('sudo reboot')


	except Exception as e:
		print(">> Ha ocurrido un error... ",e)

	except KeyboardInterrupt as e:
		print(">> Adios...")
		sys.exit()

tcpSocket.close();
tcpClienteSocket.close();
GPIO.cleanup()
