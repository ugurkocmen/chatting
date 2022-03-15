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
USERNAME = input('Choose A Username : ')

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    CLIENT_SOCKET.connect((ADDR))
except ConnectionRefusedError:
    print("Couldn't connect to the server because it's down")
    exit()

def take():
    while True:
        try:
            MESSAGE = CLIENT_SOCKET.recv(1024).decode('utf-8')
            if MESSAGE == 'USERNAME':
                CLIENT_SOCKET.send(USERNAME.encode('utf-8'))
            else:
                print(MESSAGE)
        except socket.error as ERROR_MESSAGE:
            print('Error : ', ERROR_MESSAGE)
            CLIENT_SOCKET.close()
            break

def chat():
    while True:
        MESSAGE = f'[{USERNAME}] : {input("")}'
        CLIENT_SOCKET.send(MESSAGE.encode('utf-8'))

RECEIVE_THREAD = threading.Thread(target=take)
RECEIVE_THREAD.start()

WRITE_THREAD = threading.Thread(target=chat)
WRITE_THREAD.start()
