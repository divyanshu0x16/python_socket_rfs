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
            receivedOutput = networking.receiveOutput(sock)
            print(receivedOutput)
            print(cryptoService.decryptText(receivedOutput, encryptionType))
        except ConnectionError:
            print('Socket Error')
            break
        finally:
            sock.close()
            print('Close connection to the server\n')

