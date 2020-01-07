# https://www.youtube.com/watch?v=Lbfe3-v7yE0
import socket
import time

HEADERSIZE = 10
# msg = "Welcome to the server!"
# print (f'{len(msg):<{HEADERSIZE}}' + msg)

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234)) # you can use any 4 digit port which is not occupied.
s.listen (5)    # 5 is the length of queue.
while True:
    clientsocket, address = s.accept()
    print (f"Connection from {address} has been established")
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    #clientsocket.send(bytes ("Welcome to the server!", "utf-8"))
    clientsocket.send(bytes (msg, "utf-8"))
    while True:
        time.sleep(3)
        msg = f"The time is: {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes (msg, "utf-8"))
        #clientsocket.close()