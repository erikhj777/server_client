#!/usr/bin/env python3
import socket
import threading

#this is a simple TCP chatroom program; simple server script recieves messages from any client
#then broadcasts that message to all clients connected to the chatroom
#all clients need to see what is happening in the chatroom

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 50001))

server.listen(5)

clients = [] #empty list of socket OBJs to hold new clients connecting to the server
user_ids = []

def broadcast(msg): #this method takes in a given message
    for client in clients: #iterates through each client in the clients list
        #the .send() method sends data to a socket object
        client.send(msg) #sends that message to the client

def handle(client):
    while True:
        try: #try to recieve a message from the client
            msg = client.recv(1024)
            broadcast(msg) #if get message == True broadcast to all clients
        except: #this error only occurs if the client is no longer connected
            index = clients.index(client)
            clients.remove(client) #remove client from the list
            client.close() #close connection to that clients
            user_id = user_ids[index]
            #send notice to all clients connected that a client has disconnected
            broadcast(f'{user_id} left the chat'.encode())
            user_ids.remove(user_id)
            break

def recieve():
    while True:
        client, address = server.accept() #continuously listen for new connections
        print(f'Connected with {str(address)}') #inform server admin new client connected

        #the 1st thing server does after connection is established is send keywork **USER**
        client.send('**USER**'.encode()) #this keyword prompts client to send user id
        user_id = client.recv(1024).decode() #the user id is recieved from the client
        user_ids.append(user_id) #add that client's user id to the list of user ids
        clients.append(client) #add that client to the list of clients

        print(f'User ID of the client is: {user_id}\n') #msg internally displayed for server
        client.send('Connected to the server\n'.encode())
        broadcast(f'{user_id} joined the chat\n'.encode()) #alert all users new client joined the chatroom

        #a new thread invoking the handle method is spun for ea new client
        thread = threading.Thread(target = handle, args = (client,))#run one thread for each client connected
        thread.start()

print('Server is listening...')
recieve() #need to call the recieve method to run the 'main function'
