# Scripts de Robot Explorador "Endurance" hecho con Raspberry Pi
Estos 2 scripts son el alma del robot explorador desarrollado, el cual es controlado mediante una aplicación desarrollada para Android.
Consta de:
- SendR.py
- SendS.py
Al iniciar el SO del Rasperry, estos 2 scripts deben de inicializarse.

# Descripcion general
SendR.py se encarga de escuchar las peticiónes del smartphone, y hacer avanzar el robot así como otras operaciones.

SendS.py se encarga de enviar información al smartphone sobre los sensores en el robot, como el de temperatura/humedad, y el ultrasonico, entre otros parametros.

Todo funcionando mediante sockets de red.
