#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

print ('Client: Create socket object ...')
s = socket.socket()         # Create a socket object
print ('Client: get local host name from ...')
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
print ('Client: Connect...')
print ('Client: host: ', host)
print ('Client: reserve port: ', port)
s.connect((host, port))
print ('client: s.recv(1024)')
print (s.recv(1024))
s.close()                     # Close the socket when done