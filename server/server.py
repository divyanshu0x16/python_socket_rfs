import fileService, cryptoService, networking
from socket import *

HOST = '127.0.0.1'
PORT = 12001

if __name__ == '__main__':
    listenSock = networking.createListenSocket(HOST, PORT)
    address = listenSock.getsockname()
    print('Listening on {}'.format(address))

    while True:
        clientSocket, address = listenSock.accept()
        print('Connection from {}'.format(address))

        message = networking.handleClient(clientSocket, address)
        print('{}: {}'.format(address, message))

        #TODO: Decrypt this message
        #TODO: Encrypt this message before sending

        networking.sendMessage(clientSocket, address, message, 'plain')