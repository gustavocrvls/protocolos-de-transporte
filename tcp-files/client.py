__author__ = "Gustavo Carvalho"
__date__ = "14/02/2021"

import socket

TCP_IP = '127.0.0.1' # IP do Servidor
PORT = 5500 # Porta do Servidor

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um novo socket
tcp.connect((TCP_IP, PORT)) # Cria uma nova conexão

message = input('Enter File Name: ') # Mensagem que será enviada para o servidor

tcp.send(bytes(message, 'UTF-8')) # Envia o dado

data = tcp.recv(1024) # Captura a resposta

# print("received data: ", data.decode('UTF-8', 'strict')) # Escreve a mensagem recebida no terminal

f = open("new__" + message, 'wb') # Cria um novo arquivo com o nome enviado
f.write(data) # Escreve o conteúdo recebido nesse novo arquivo
# if data.decode('UTF-8', 'strict') != 'file not found': # Caso um arquivo seja recebido

tcp.close() # Fecha a conexão
