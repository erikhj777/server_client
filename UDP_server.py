#!/usr/bin/env python3
from datetime import datetime
import socket

print(f'Starting server at {datetime.now()}')
print(f'Waiting for client...')
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 6789))

data, client = server.recvfrom(4096)

print(f'At {datetime.now()} {client} said {data}')
server.sendto(b'Are you talking to me?', client) #data encoded as b'' instead of using .encode() method
server.close()
