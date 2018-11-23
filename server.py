#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

if len(sys.argv) == 4:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    if os.path.exists(sys.argv[3]):
        audio_fich = sys.argv[3]
    else:
        sys.exit("Usage: <IP><PORT><cancion.mp3>")
else:
    sys.exit("Usage: python3 server.py IP port audio_file")
    

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        #self.wfile.write(b"Hemos recibido tu peticion")
        
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
           # print(line.decode('utf-8'))
           # Si no hay más líneas salimos del bucle infinito
            if  len(line) == 0:
                break
            # compruebo si recibo un invite y le envio la respuesta
            elif line.decode('utf-8').split(" ")[0] == "Invite" :
                print("El cliente nos manda " + line.decode('utf-8'))
                self.wfile.write(b"SIP/2.0 100 Trying SIP/2.0 180 Ringing SIP/2.0 200 OK.")
            elif line.decode('utf-8').split(" ")[0] == "Ack" :
                os.system('mp32rtp -i 127.0.0.1 -p 23032 < ' + audio_fich)
                print("El cliente nos manda " + line.decode('utf-8'))
            elif line.decode('utf-8').split(" ")[0] == "Bye" :
                print("El cliente nos manda " + line.decode('utf-8'))
                self.wfile.write(b" 200 ok")
            elif line.decode('utf-8').split(" ")[0] != ("Invite" or "Ack"):
                self.wfile.write(b"SIP/2.0 405 Method Not Allowed")
 
                
           
if __name__ == "__main__":
    try:
        # Creamos servidor de eco y escuchamos
        serv = socketserver.UDPServer((IP, PORT), EchoHandler)
        print("Listening...")
        serv.serve_forever()
    except:
        print("Keyboard Interrupt")
