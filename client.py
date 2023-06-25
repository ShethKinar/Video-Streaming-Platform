import socket
import threading
import time

PORT = 5050
FORMAT = 'utf-8'
SERVER = '20.124.214.215'
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "haltino tha"

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def receive():

    msg_length = (client.recv(HEADER).decode(FORMAT))
    if msg_length:
        msg_length = int(msg_length)
        msg = client.recv(msg_length).decode(FORMAT)
        print(f"{SERVER} said that  \"{msg}\"")


entr = client.recv(HEADER).decode(FORMAT)
print(entr)
name = input()
client.send(name.encode(FORMAT))
time.sleep(1)
while True:
    msg = input("Enter a message: ")
    if msg == DISCONNECT_MESSAGE:
        client.close()
        break
    else:
        send(msg)
        receive()
        time.sleep(0.2)
