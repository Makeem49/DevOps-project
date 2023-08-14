import socket
import time

MAX_SIZE_BYTES = 65535

# Setting up a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
port = 3000
hostname = '127.0.0.1'
s.bind((hostname, port)) # Binding the socket to a port and IP address
print('Listening at {}'.format(s.getsockname())) # Printing the IP address and port of socket

while True:
    data, clientIpAddress = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    data.decode()
    upperCaseMessage = message.upper()
    data = upperCaseMessage.encode('ascii')
    s.sendto(data, clientIpAddress)    