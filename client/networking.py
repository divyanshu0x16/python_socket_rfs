def sendCommand(socket, command, encryptionType):
    command += '\0'
    socket.sendall(command.encode('utf-8'))
    return 0

def receiveOutput(socket):
    receivedOutput = socket.recv(4096)
    return receivedOutput

