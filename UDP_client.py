#!/usr/bin/env python3
from datetime import datetime
import socket

print('Starting the client now')
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'Hey', ('127.0.0.1', 6789))
data, server = client.recvfrom(4096)
print(f'At {datetime.now()} {server} said {data}')
client.close()
