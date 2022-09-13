import sys, socket
import fileService, cryptoService, networking

HOST = '127.0.0.1'
PORT = 12001

if __name__ == '__main__':
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            print('\nConnected to {}:{}'.format(HOST, PORT))

            command = fileService.takeInput()

            if command == 'q':
                break

            encryptedCommand, encryptionType = cryptoService.encryptText(command)
            networking.sendCommand(sock, encryptedCommand, encryptionType)

            if( command.startswith('dwd ') ):
                data, fileName = networking.receivedFile(sock)

                decryptedData = cryptoService.decryptText(data, encryptionType)
                decryptedName = cryptoService.decryptText(fileName, encryptionType)

                if('NOK' in decryptedName):
                    print('invalid file requested')
                    print('NOK')
                else:
                    fileService.writeFile(decryptedData, decryptedName)

                    receivedOutput = networking.receiveOutput(sock)
                    print(cryptoService.decryptText(receivedOutput, encryptionType))
            elif( command.startswith('upd ')):
                data, fileName = fileService.readFile(command)

                encryptedName = cryptoService.encryptText(fileName, encryptionType)[0]
                encryptedData = cryptoService.encryptText(data, encryptionType)[0]

                networking.sendFile(sock, encryptedData, encryptedName)

                receivedOutput = networking.receiveOutput(sock)
                print(cryptoService.decryptText(receivedOutput, encryptionType))
            else:
                receivedOutput = networking.receiveOutput(sock)
                print(cryptoService.decryptText(receivedOutput, encryptionType))

        except ConnectionError:
            print('Socket Error')
            break
        finally:
            sock.close()
            print('Close connection to the server\n')

