import socket
from threading import Thread


name = input("Enter Your Name: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("Localhost", 2002))

client.send(name.encode())


def send(cleint):
    while True:
        data = str(name)+":"+str(input(""))
        client.send(data.encode())


def receive(client):
    while True:
        try:
            data = client.recv(2222).decode()
            print(data)
        except:
            client.close()
            break


thread1 = Thread(target=send, args=(client,))
thread1.start()
thread2 = Thread(target=receive, args=(client,))
thread2.start()
