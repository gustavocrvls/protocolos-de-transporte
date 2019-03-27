__author__ = "Gustavo Carvalho"
__date__ = "25/03/2018"

import socket

TCP_IP = '127.0.0.1' # IP do Servidor
PORT = 5500 # Porta que ficará aberta
BUFFER = 1024 # Buffer

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um novo socket
tcp.bind((TCP_IP, PORT)) # Liga o socket ao endereço e porta
tcp.listen(1) # Faz com que o servidor fique escutando

print('Server online\nIP: ', TCP_IP, ' Port: ', PORT)

conn, addr = tcp.accept() # Recebe uma nova requisição

print('Connection address:', addr)

while 1:
    data = conn.recv(BUFFER) # Recebe os dados
    if not data:
    	print('Data not found! Closing Server...')
    	break
    return_data = ''
    return_data += '\n data: ' + str(data.decode('UTF-8', 'strict')).upper()
    return_data += '\n tdata_length: ' + str(len(data))
    conn.send(bytes(return_data, 'UTF-8')) # Envia os dados ao cliente

tcp.close() # Fecha a conexão
