# https://www.youtube.com/watch?v=Lbfe3-v7yE0
import socket
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234)) # you can use any 4 digit port which is not occupied.
s.listen (5)    # 5 is the length of queue.
while True:
    clientsocket, address = s.accept()
    print (f"Connection from {address} has been established")
    clientsocket.send(bytes ("Welcome to the server!", "utf-8"))
    clientsocket.close()