def sendCommand(socket, command, encryptionType):
    #TODO: Send encryption types here
    command += '\0'
    socket.sendall(command.encode('utf-8'))
    return 0

def receiveOutput(socket):
    data = bytearray()
    msg = ''
    while not msg:
        recvd = socket.recv(4096)
        if not recvd:
            raise ConnectionError()
        data = data + recvd
        if b'\0' in recvd:
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

