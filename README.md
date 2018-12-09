# Scripts de Robot Explorador "Endurance" hecho con Raspberry Pi
Estos 2 scrips son el alma del robot explorador desarrollado, el cual es controlado mediante una aplicación desarrollada para Android.
Consta de:
- SendR.py
- SendS.py

# Descripcion general
SendR.py se encarga de escuchar las peticiónes del smartphone, y hacer avanzar el robot así como otras operaciones.

SendS.py se encarga de enviar información al smartphone sobre los sensores en el robot, como el de temperatura/humedad, y el ultrasonico, entre otros parametros.

Todo funcionando mediante sockets de red.
