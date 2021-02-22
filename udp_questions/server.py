__author__ = "Gustavo Carvalho"
__date__ = "25/03/2018"

import socket

UDP_IP = "127.0.0.1" # IP do Servidor
UDP_PORT = 5005 # Porta do Servidor
BUFFER = 1024 # Buffer

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria novo socket
sock.bind((UDP_IP, UDP_PORT)) # Liga o socket ao IP e Porta

while True:
  data, addr = sock.recvfrom(1024) # Recebe os dados
  
  print('Connection address:', addr)

  if data:
    answer = data.decode('UTF-8', 'strict').split(';') # separa o datagrama recebido em um array
    with open('questions.txt', "r") as f: # abre o arquivo de questoes
      try:
        bytes_read = f.readlines(BUFFER) # lê as linhas do arquivo
        q = bytes_read[int(answer[0]) - 1].split(';') # busca a linha que corresponde à questão recebida
        a = list(q[2].replace('\n', '')) # retira os \n e transforma as alternativas em uma lista
        
        iguais = 0
        diferentes = 0

        # faz a contagem de questões iguais e diferentes
        for i in range(int(answer[1])):
          if list(answer[2])[i] == a[i]:
              iguais = iguais + 1
          else:
              diferentes = diferentes + 1

        print ("questão: ", answer[0])
        print ("certas: ", iguais)
        print ("erradas: ", diferentes)
        sock.sendto(bytes(q[0] + ';' + str(iguais) + ';' + str(diferentes), 'UTF-8'), addr) # envia ao cliente a contagem das questões certas e erradas
      except:
        sock.sendto(bytes('Formato de questão não suportado!', 'UTF-8'), addr) # caso o datagrama recebido seja invalido, retorna um erro
