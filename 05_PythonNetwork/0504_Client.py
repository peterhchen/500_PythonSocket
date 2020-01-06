# https://www.youtube.com/watch?v=Lbfe3-v7yE0
import socket
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect ((socket.gethostname(), 1234))
full_msg = '';
while True:
    msg = s.recv (8) # receive 8 bytes of data at a time
    if (len (msg) <= 0):
        break
    else:
        full_msg += msg.decode ('utf-8')

print ('full_msg: ', full_msg)