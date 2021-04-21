#!/usr/bin/env python3

import socket
import time
#instantiate server socket object
#server will be left continually running to communicate with clients as needed
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((socket.gethostname(), 9999)) #bind serv to localhost port 9999

#.listen() method enables server to recieve incomming connections
#accepts 1 param which is # of unaccepted connection server will allow
#before dropping new connections
serv.listen(5)

while True:
    #.accept() method waits for incomming connections
    #it creates a new socket obj for ea new connection
    #returns 2 values Socket OBJ & Addr info
    conn, addr = serv.accept() #conn in the socket obj for the connection
    #conn is able to send and recieve data for that specific connection
    print(f'Got a connection from {addr}')
    currentTime = time.ctime(time.time()) + "\r\n"
    #in python3 all strings are unicode
    #so any text send through a socket needs to be encoded
    conn.send(currentTime.encode('ascii'))
    #.close() method marks the socket as closed; all subsequent ops will fail
    conn.close()
#==============================================================================
    # while True:
    #
    #     #call .recieve() to get data from that individual client
    #     data = conn.recv(4096) #recieve data 4096 bytes at a time
    #     if not data: #break out of loop when no more data to recieve
    #         break
    #     from_client += data #append data to from_client str
    #
    #     print(from_client) #return the completed message from ea client
    #     conn.send('I am a server')
    #
    # conn.close()
    # print('Client disconnected')
