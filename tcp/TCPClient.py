import socket

HOST = '127.0.0.1'
PORT = 5500
MESSAGE = "It's Alive!"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((HOST, PORT))

tcp.send(bytes(MESSAGE, 'UTF-8'))

data = tcp.recv(1024)

print("received data: ", data)

tcp.close()
