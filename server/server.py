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

        message, encryptionType = networking.handleClient(clientSocket, address)
        if(message == 'Error'):
            print('Socket Error')

        decryptedCommand = cryptoService.decryptText(message, int(encryptionType))
        
        #TODO: Run the command and get output

        encryptedMessage = cryptoService.encryptText(decryptedCommand, int(encryptionType))

        networking.sendMessage(clientSocket, address, encryptedMessage)