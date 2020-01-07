#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
print ('Server: create socket object ...')
s = socket.socket()         # Create a socket object
print ('Server: get local host name ...')
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
print ('Server: bind the host to port ...')
print ('Server: host: ', host)
print ('Server: port:', port)
s.bind((host, port))        # Bind to the port
print ('Server: wait and listen ...')
s.listen(5)                 # Now wait for client connection.
while True:
    print ('Server: accept')
    c, addr = s.accept()     # Establish connection with client.
    print ('Server: Got connection from', addr)
    #clientsocket.send(bytes ("Welcome to the server!", "utf-8"))
    c.send(bytes ('Thank you for connecting', 'utf-8'))
    c.close()                # Close the connection