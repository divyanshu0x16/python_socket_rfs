import socket

def createListenSocket(host, port):
    # Setup the sockets our server will receive connection requests on 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(100)
    return sock

def recvMessage(sock):
    # Wait for data to arrive on the socket, then parse into
    # messages using b'\0' as message delimiter
    data = bytearray()
    msg = ''
    # Repeatedly read 4096 bytes off the socket, storing the bytes
    # in data until we see a delimiter
    while not msg:
        recvd = sock.recv(4096)
        if not recvd:
            # Socket has been closed prematurely
            raise ConnectionError()
        data = data + recvd
        if b'\0' in recvd:
            # we know from our protocol rules that we only send
            # one message per connection, so b'\0' will always be
            # the last character
            msg = data.rstrip(b'\0')
    msg = msg.decode('utf-8')
    return msg

def handleClient(sock, address):
    # Receive data from the client via socket and process it further
    try:
        msg = recvMessage(sock)
        return msg
    except ( ConnectionError, BrokenPipeError ):
        print('Socket Error')
    finally:
        print('Closed connection to {}'.format(address))
        sock.close()