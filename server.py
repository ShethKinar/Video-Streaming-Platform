import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!disconnect"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(socket.port)
print(SERVER)
# print(server.getsockname()[1])

try: 
    server.bind(ADDR)
except socket.error as e:
    print(e)




# def recive_client_name(conn):
#     msg_length = (conn.recv(HEADER).decode(FORMAT))
#     if msg_length:
#         msg_length = int(msg_length)
#         msg = conn.recv(msg_length).decode(FORMAT)
#         print(f"{SERVER} said that  \"{msg}\"")





def handle_client(conn, addr):
    print("New connection: ", str({addr}) , "connected.")
    connected = True
    conn.send("Please enter your name: ".encode(FORMAT))
    client_name = conn.recv(HEADER).decode(FORMAT)
    

    while connected:
        msg_length = (conn.recv(HEADER).decode(FORMAT))
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(str({client_name})+ ": " + str(msg))
            send((str({client_name})+ "'s msg has been received\n"), conn)
            if msg==DISCONNECT_MESSAGE:
                print(str({addr}) +" disconnected.")
                send(("Bye " +str({client_name})), conn)
                connected = False
    conn.close()


def send(msg, conn):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    conn.send(send_length)
    conn.send(message)



def ask_client_name(conn,addr):
    send("Please enter your name: ",conn)
    client_name = conn.recv(1024).decode(FORMAT)
    return client_name
    
    

def start():
    server.listen()
    print("Listening to server " +str({SERVER}))
    while True:
        conn, addr = server.accept()
        # client_name = ask_client_name(conn,addr)
        thread = threading.Thread(target=handle_client, args=(conn, addr))

        thread.start()
        print("Active connections: " + str({threading.active_count() - 1}))


print("Server started")

start()
# server.close()
