import socket, threading, sys

HOST = "127.0.0.1"  # configura o ip hospedeiro para a conexao
PORT = 2023  # porta de comunicacao (a mesma que a do servidor)

def handleConnection(conn, addr):
    data = conn.recv(1024)
    message = data.decode('ascii').split()

    print("Dados recebidos: ", message)

    confirmation = "ACK"
    conn.send(bytes(confirmation, 'ascii')) 
    
    conn.close()    

def handleInput(serverSocket):
    print("Digite 1 para enviar um 'hello' ou 2 encerrar o processo.")
    while True:
      opcao = int(input())
      print("Opcao escolhida -> %d", opcao)
      if opcao == 1:
        # serverSocket.connect(("127.0.0.1", 2022))
        message = "hello thread"
        print('Enviando "' + message + '" para o servidor...')
        serverSocket.send(message.encode('ascii'))
        data = sock.recv(1024)
        print('Recebido do servidor: ',str(data.decode('ascii')))
        # sock.close()
      elif opcao == 2:     
        # encerrar execucao
        # NAO FUNCIONA
        # break;
        sys.exit()
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind((HOST, PORT));
    serverSocket.listen(2); # 2 = number of connections

    print('Server iniciado em ' + HOST + ':' + str(PORT))
    
    # obtem inputs do usuario (usado para mandar mensagens)
    inputThread = threading.Thread(target = handleInput, args=(serverSocket,))
    inputThread.start()

    # espera conexao
    while True:
        conn, addr = serverSocket.accept()
        x = threading.Thread(target=handleConnection, args=(conn, addr))
        x.start()

    serverSocket.close()