__author__ = "Gustavo Carvalho"
__date__ = "25/03/2018"

import socket

UDP_IP = "127.0.0.1" # IP do Servidor
UDP_PORT = 5005 # Porta do Servidor

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria novo socket
sock.bind((UDP_IP, UDP_PORT)) # Liga o socket ao IP e Porta

while True:
    data, addr = sock.recvfrom(1024) # Recebe os dados
    print ("original received data: ", data.decode('UTF-8', 'strict'))
    print ("data_size: ", len(data))
    print ("Upper: ", data.decode('UTF-8', 'strict').upper())
