import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("Localhost", 2002))

server.listen()
all_clients = {}


def client_thread(client):
    while True:
        try:
            msg = client.recv(2222)
            for i in all_clients:
                i.send(msg)
        except:
            for i in all_clients:
                if i != client:
                    i.send(f"{name} exit".encode())
            del all_clients[client]
            client.close()
            break


while True:
    print("Waiting for connection.....")
    client, address = server.accept()
    print("connection Established")
    name = client.recv(1024).decode()
    all_clients[client] = name
    for c in all_clients:
        if c != client:
            c.send(f"{name} already Joined".encode())
    thread = Thread(target=client_thread, args=(client,))
    thread.start()
