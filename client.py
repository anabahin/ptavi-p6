#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.
usage_error = "Usage: python3 client.py method receiver@IP:SIPport"

# Dirección IP del servidor.
if len(sys.argv) != 3 :
    sys.exit("Usage: Number of Arguments must be 2")
    
try:
    Metodo = sys.argv[1]
    # voy a separa mi segundo argumento en partes
    Dividir = sys.argv[2].split('@')
    login = Dividir[0]
    Dividir2 = Dividir[1].split(':')
    Ip = Dividir2[0]
    Port = int(Dividir2[1])
except:
    sys.exit(usage_error)


     

# Contenido que vamos a enviar
LINE = Metodo + ' SIP:' + sys.argv[2].split(':')[0] + 'SIP/2.0' 

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((Ip, Port))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n\r\n')
    data = my_socket.recv(1024)

        

    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
