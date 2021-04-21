#!/usr/bin/env python3

import socket

server = socket.socket() #use default settings
server.bind((socket.gethostname(), 12345))

server.listen(1)

conn, addr = server.accept()
print(f'Connected to {addr}')

while True:

    data = conn.recv(1024) #data recieved on new connection's socket object
    if not data:
        break
    conn.sendall(data)

conn.close()
