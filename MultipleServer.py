'''

DOCSTRING : It's application for chatting. I developed this application for my Cyber Security Teacher.

How Can We Use?

You need choose a username for users. If you do it, you can use it. When you choose your username, everybody can see your username.
The server will forward all the messages to your screen for you.

Developer : Uğur Koçmen
'''

import socket
import threading

HOST = "127.0.0.1"
PORT = 7777

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.bind((HOST,PORT))
SERVER_SOCKET.listen()

CLIENT_LIST = []
USERNAME_LIST = []

def broadcast(MESSAGE):
    for CLIENT in CLIENT_LIST:
        CLIENT.send(MESSAGE)

def handle(CLIENT):
    while True:
        try:
            MESSAGE = CLIENT.recv(1024)
            broadcast(MESSAGE)
        except:
            INDEX = CLIENT_LIST.index(CLIENT)
            CLIENT.close()
            USERNAME = USERNAME_LIST[INDEX]
            broadcast (f'{USERNAME} Left The Chat!'.encode('utf-8'))
            USERNAME_LIST.remove(USERNAME)
            break

def receive():
    while True:
        CLIENT, ADDRESS = SERVER_SOCKET.accept()
        print(f'Connected With {str(ADDRESS)}')

        CLIENT.send("USERNAME".encode('utf-8'))
        USERNAME = CLIENT.recv(1024).decode('utf-8')
        USERNAME_LIST.append(USERNAME)
        CLIENT_LIST.append(CLIENT)

        print(f'Username Of The Client Is {USERNAME}!')
        broadcast(f'{USERNAME} Joined The Chat! Welcome!'.encode('utf-8)'))
        CLIENT.send("Connected To The Server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(CLIENT, ))
        thread.start()

print("Server Is Listening...")
receive()
