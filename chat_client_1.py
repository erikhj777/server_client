#!/usr/bin/env python3
import socket
import threading

user_id = input('Enter a user id:')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 50001)) #when run it triggers server accept method

def recieve(): #continuously recieving new messages
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg == '**USER**': #check for '**USER**' keyword as cue to send user id
                client.send(user_id.encode())
            else: print(msg) #otherwise just print the message from the server
        except:
            print('An error occured!')
            client.close()
            break

def write(): #continuously have option to send new msg -> server and then all connected clients
    while True:
        msg = f'{user_id}: {input("")}\n' #must use different quotes inside and outside the f string
        client.send(msg.encode())

#need to define two thread to be able to send and recieve data at same time
#with these two threads the recieve and write functions will run simultaneously
recieve_thread = threading.Thread(target = recieve)
recieve_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()
