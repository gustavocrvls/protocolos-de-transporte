__author__ = "Gustavo Carvalho"
__date__ = "21/02/2020"

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
BUFFER = 1024 # Buffer

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Cria novo socket

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)

while True:
  # Recebe os valores do formulário
  print('----------------------------')
  questao = input('Questão: ')
  qtd = input('Quantidade de Alternativas: ')
  alternativas = input('Alternativas (V,F): ')

  # Caso o número de alternativas recebidas esteja correto
  if (len(list(alternativas)) == int(qtd)):
    sock.sendto(bytes(questao + ';' + qtd + ';' + alternativas, 'UTF-8'), (UDP_IP, UDP_PORT)) # Envia os dados ao servidor

    data = sock.recv(BUFFER) # recupera os dados

    response = data.decode('UTF-8', 'strict').split(';') # decodifica os dados recebidos
    if (len(response) == 3):
      print('Questão: ', response[0])
      print('Acertos: ', response[1])
      print('Erros: ', response[2])
    else:
      print('Número inválido de alternativas')

  else:
    print('Número inválido de alternativas')