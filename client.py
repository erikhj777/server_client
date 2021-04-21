#!/usr/bin/env python3

import socket

#create the client socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost = socket.gethostname()
#open the client socket object; this will only happen if serv alread running
client.connect((localhost, 9999))

tm = client.recv(1024) #recieves no more than 1024 bytes
client.close()

print(f'Time recieved was {tm}')
#==============================================================================
# #send a data string to the socket
# msg = 'I am a client, give me service!'
# bin_msg = [format(i, '08b') for i in msg]
# client.send(bin_msg)
#
# #while open, also enable client to recieve msg from serv
# from_serv = client.recieve(4096)
#
# client.close() #tear down open connection
#
# print(from_serv)
