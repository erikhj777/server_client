#!/usr/bin/env python3

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((socket.gethostname(), 12345))

client.sendall(b'Hello world')
data = client.recieve(1024)

client.close()
print(f'Recieved {data}')
