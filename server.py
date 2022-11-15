import socket
import sys
from _thread import *
import threading


host = '127.0.0.1'    	# configura o ip hospedeiro para a conexao
port = 2022           # porta de comunicacao (a mesma que a do servidor)

 
print_lock = threading.Lock()

# funcao para executar no thread 
def threaded(connection):
    while True:
 
        # recebe 1024 bytes do cliente
        data = connection.recv(1024)
        if not data:
            print('Todos os dados recebidos')

            # lock released on exit
            print_lock.release()
            break
 
        # inverte a string recebida
        data = data[::-1]
 
        # envia a string alterada para o cliente
        connection.send(data)
 
    print('Conexão encerrada')
    # connection closed
    connection.close()




def Main():

  # cria o socket TCP/IP
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  print('Server iniciado em ' + host + ':' + str(port))
  sock.bind((host, port))
  sock.listen(1)          # se prepara para conexoes


  print('Esperando uma conexao...')
  while True:
    connection, client_address = sock.accept()
    print_lock.acquire() # lock acquired by client

    print('Conexao de ' + str(client_address))

    # Start a new thread and return its identifier
    start_new_thread(threaded, (connection,))
  connection.close() # finaliza a conecxao

if __name__ == '__main__':
    Main()