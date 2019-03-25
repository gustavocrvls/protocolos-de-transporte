import socket

TCP_IP = '127.0.0.1'
PORT = 5500

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((TCP_IP, PORT))
tcp.listen(1)

conn, addr = tcp.accept()

print ('Connection address:', addr)

while 1:
    data = conn.recv(1024)
    if not data: break
    print("re")
    conn.send(data)
tcp.close()
