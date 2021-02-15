# TCP - Files

Este é um exemplo simples de um servidor TCP que recebe uma mensagem de um cliente contendo o nome de um arquivo, pesquisa na pasta do servidor se há algum arquivo desse nome e retorna para o cliente que então cria um novo arquivo com o conteúdo recebido.

### Como executar:

- Obs: Necessário ter o Python instalado.

1. Inicie o servidor com o comando:

```
  python server.py
```
ou dependendo da sua máquina
```
  python3 server.py
```

2. Inicie o cliente com o comando:

```
  python client.py
```
ou dependendo da sua máquina
```
  python3 client.py
```

3. No cliente, insira o nome de um arquivo.

- Arquivos de teste existentes nesse exemplo:
  - test.txt
  - test2.json