#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.

# Dirección IP del servidor.
if len(sys.argv) != 3 :
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")
    
try:
    Metodo = sys.argv[1]
    # voy a separa mi segundo argumento en partes
    Dividir = sys.argv[2].split('@')
    login = Dividir[0]
    Dividir2 = Dividir[1].split(':')
    Ip = Dividir2[0]
    Port = int(Dividir2[1])
except:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

# Contenido que vamos a enviar
LINE = Metodo + ' SIP:' + sys.argv[2].split(':')[0] + ' SIP/2.0' 

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((Ip, Port))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n\r\n')
    data = my_socket.recv(1024)

    if data.decode('utf-8').split(" ")[1] == "100":
        print('Recibido la respuesta: -- ', data.decode('utf-8'))
        LINE_ACK = "ACK" + ' SIP:' + sys.argv[2].split(':')[0] + ' SIP/2.0' 
        print("Enviando: " + LINE_ACK )
        my_socket.send(bytes(LINE_ACK, 'utf-8') + b'\r\n\r\n')
    if data.decode('utf-8').split(" ")[0] == "200":
        print("El servidor ha recibido mi ACK")
        
    print("Terminando socket...")

print("Fin.")
