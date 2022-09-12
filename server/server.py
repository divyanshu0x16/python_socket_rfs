import fileService, cryptoService, networking
from socket import *

HOST = '127.0.0.1'
PORT = 12001

# serverSocket = socket(AF_INET,SOCK_STREAM)
# serverSocket.bind(("",serverPort))

# serverSocket.listen(1)

# print("The server is ready to receive")

# while True:
#     connectionSocket, addr = serverSocket.accept()
    
#     encryptedCommand = connectionSocket.recv(1024)
#     encryptionType = 'plain'

#     command = cryptoService.decryptText(encryptedCommand, encryptionType)
#     #We will run this command and do something

#     connectionSocket.send(command)
#     connectionSocket.close()

if __name__ == '__main__':
    listenSock = networking.createListenSocket(HOST, PORT)
    address = listenSock.getsockname()
    print('Listening on {}'.format(address))

    while True:
        clientSocket, address = listenSock.accept()
        print('Connection from {}'.format(address))

        message = networking.handleClient(clientSocket, address)
        print('{}: {}'.format(address, message))