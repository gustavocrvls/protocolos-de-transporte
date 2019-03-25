import socket

TCP_IP = '127.0.0.1'
PORT = 5500
BUFFER = 1024

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((TCP_IP, PORT))
tcp.listen(1)

print('Server online\nIP: ', TCP_IP, ' Port: ', PORT)

conn, addr = tcp.accept()

print('Connection address:', addr)

while 1:
    data = conn.recv(BUFFER)
    if not data:
    	break
    return_data = ''
    return_data += 'data: ' + str(data).upper()
    return_data += '  __  tdata_length: ' + str(len(data))
    conn.send(bytes(return_data, 'UTF-8'))

tcp.close()
