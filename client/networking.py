def sendCommand(socket, command, encryptionType):
    command += '&' + str(encryptionType) + '\0'
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

def receivedFile(socket):
    try:
        fileName = socket.recv(4096).rstrip(b'\0').decode('utf-8')
        data = socket.recv(4096)

        return data, fileName
    except:
        raise ConnectionError()

def sendFile(sock, file, fileName):
    fileName = fileName + '\0'
    try:
        print('Sending FileName... ')
        sock.sendall(fileName.encode('utf-8'))
        print('Sending Data... ')
        sock.sendfile(file)
    except ( ConnectionError, BrokenPipeError ):
        raise ConnectionError()

