__author__ = "Gustavo Carvalho"
__date__ = "25/03/2018"

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
# MESSAGE = "Hello, World!"

message = input('Enter Something: ')

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", message)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria novo socket
sock.sendto(bytes(message, 'UTF-8'), (UDP_IP, UDP_PORT)) # Envia os dados
