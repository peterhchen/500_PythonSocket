# https://www.youtube.com/watch?v=Lbfe3-v7yE0
import socket
import time
import pickle

HEADERSIZE = 10
# msg = "Welcome to the server!"
# print (f'{len(msg):<{HEADERSIZE}}' + msg)

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234)) # you can use any 4 digit port which is not occupied.
s.listen (5)    # 5 is the length of queue.
while True:
    clientsocket, address = s.accept()
    print (f"Connection from {address} has been established")

    # some arbitrary python object
    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)
    print (msg)
    msg = bytes (f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    
    clientsocket.send(bytes (msg))
