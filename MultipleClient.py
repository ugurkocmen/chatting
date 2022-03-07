'''

DOCSTRING : It's application for chatting. I developed this application for Kaan Tekiner.

How Can We Use?

You need choose a username for application. If you do it, you can use it. When you choose your username, everybody
can see your username.

Developer : Uğur Koçmen
Instagram : ukocmenn
GitHub : github.com/ugurkocmen

'''

import socket
import threading

HOST = "127.0.0.1"
PORT = 7777
USERNAME = input('Choose A Username : ')

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT_SOCKET.connect((HOST,PORT))

def receive():
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

def write():
    while True:
        MESSAGE = f'[{USERNAME}] : {input("")}'
        CLIENT_SOCKET.send(MESSAGE.encode('utf-8'))

RECEIVE_THREAD = threading.Thread(target=receive)
RECEIVE_THREAD.start()

WRITE_THREAD = threading.Thread(target=write)
WRITE_THREAD.start()