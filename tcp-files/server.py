__author__ = "Gustavo Carvalho"
__date__ = "14/02/2021"

import socket

TCP_IP = '127.0.0.1' # IP do Servidor
PORT = 5500 # Porta que ficará aberta
BUFFER = 1024 # Buffer

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Cria um novo socket
tcp.bind((TCP_IP, PORT)) # Liga o socket ao endereço e porta
tcp.listen(1) # Faz com que o servidor fique escutando

print('Server online\nIP: ', TCP_IP, ' Port: ', PORT)


while True:
    conn, addr = tcp.accept() # Recebe uma nova requisição

    print('Connection address:', addr)
    
    data = conn.recv(BUFFER) # Recebe os dados

    if data:
        try:
            print(data.decode('UTF-8', 'strict'))
            with open('./files/' + data.decode('UTF-8', 'strict'), "rb") as f: # Tenta ler o arquivo no disco
                bytes_read = f.read(BUFFER)
                print(bytes_read)
                conn.sendall(bytes_read) # Envia o conteúdo do arquivo
        except:
            conn.send(bytes('file not found', 'UTF-8')) # Caso não encontre envia uma mensagem

tcp.close() # Fecha a conexão
