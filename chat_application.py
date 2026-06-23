# Chat Application using Python Sockets

import socket
import threading

HOST = "127.0.0.1"
PORT = 5555

mode = input("Run as server (s) or client (c)? ").lower()

if mode == "s":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    clients = []

    def broadcast(message):
        for client in clients:
            client.send(message)

    def handle(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message)
            except:
                clients.remove(client)
                client.close()
                break

    print("Server started and waiting for connections...")

    while True:
        client, address = server.accept()
        print("Connected:", address)
        clients.append(client)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

else:
    nickname = input("Enter your nickname: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    def receive():
        while True:
            try:
                message = client.recv(1024).decode()
                print(message)
            except:
                print("Connection closed.")
                client.close()
                break

    def send_message():
        while True:
            message = input()
            client.send(f"{nickname}: {message}".encode())

    threading.Thread(target=receive).start()
    threading.Thread(target=send_message).start()
