import socket
import sys

# cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'    	# configura o ip hospedeiro para a conexao
port = 2001           # porta de comunicacao (a mesma que a do servidor)

def Main():
  try:
      print('Se conectando a ' + host + ':' + str(port))
      sock.connect((host, port))  # conecta o socket na porta em que o server esta escutando

      opcao = int(input("Digite 1 para enviar ou 2 para receber um arquivo: "))
      if opcao == 1:       # enviar
          # sock.sendall(bytes([1]))      # avisa o servidor que o cliente vai ENVIAR um arquivo
          # message sent to server

          try:
              message = "hello outro thread"
              print('Enviando "' + message + '" para o servidor...')
              sock.send(message.encode('ascii'))
              
              # message received from server
              data = sock.recv(1024)
              print('Recebido do servidor: ',str(data.decode('ascii')))

              # ans = input('\Deseja enviar outra mensagem (y/n):')
              # if ans == 'y':
              #     continue
              # else:
              #     break
          except Exception as ex:
              print(ex)
      else:   
          print("Opcao invalida.")

  finally:
      sock.close()
      print('Socket fechado.')


if __name__ == '__main__':
    Main()


