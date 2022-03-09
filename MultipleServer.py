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
ADDR = (HOST,PORT)

SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.bind((HOST,PORT))
SERVER_SOCKET.listen()

CLIENT_LIST = []
USERNAME_LIST = []

# sends a message to all CLIENT in the CLIENT_LIST.

def broadcast(MESSAGE, SENDER):
    for CLIENT in CLIENT_LIST:
        if CLIENT == SENDER: continue
        CLIENT.send(MESSAGE)

# receives the message from the CLIENT and sends it to the broadcast function.

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

# Accepts connections. Clients join the server.
            
def take():
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

        thread = threading.Thread(target=handle, args=(CLIENT, ), daemon=True) # Used to connect customers at the same time.
        thread.start()                                                         # Customers will send messages, we have to process them.

print("Server Is Listening...")
take()
