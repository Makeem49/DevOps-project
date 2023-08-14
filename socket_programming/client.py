import socket

MAX_SIZE_BYTES = 65535

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 12345))
message = input('Input lowercase sentence:' )
data = message.encode('ascii')
s.sendto(data, ('127.0.0.1', 3000))
print('The OS assigned the address {} to me'.format(s.getsockname()))
data, address = s.recvfrom(MAX_SIZE_BYTES) 
text = data.decode('ascii')
print(address, data)