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
            print('Connection Closed')
            continue

        decryptedCommand = cryptoService.decryptText(message, int(encryptionType))
        
        if( decryptedCommand.startswith('dwd ') ):

            try:
                file, fileName = fileService.handleCommand(decryptedCommand)

                encryptedName = cryptoService.encryptText(fileName, int(encryptionType))

                networking.sendFile(clientSocket, file, encryptedName)
                networking.sendMessage(clientSocket, address, cryptoService.encryptText('OK', int(encryptionType)))
            except ( ValueError ):
                networking.sendMessage(clientSocket, address, cryptoService.encryptText('NOK', int(encryptionType)))

        elif( decryptedCommand.startswith('upd ')):

            try:
                data, fileName = networking.receiveFile(clientSocket)

                decryptedData = cryptoService.decryptText(data, int(encryptionType))
                decryptedName = cryptoService.decryptText(fileName, int(encryptionType))

                fileService.writeFile(decryptedData, decryptedName)
                networking.sendMessage(clientSocket, address, cryptoService.encryptText('OK', int(encryptionType)))
            except:
                networking.sendMessage(clientSocket, address, cryptoService.encryptText('NOK', int(encryptionType)))

        else:
            output = fileService.handleCommand(decryptedCommand)
            encryptedMessage = cryptoService.encryptText(output, int(encryptionType))
            networking.sendMessage(clientSocket, address, encryptedMessage)