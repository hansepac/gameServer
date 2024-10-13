from __init__ import *
import socket

def connect_to_server():
    """Connect to the game server and send messages."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to server.")
    while True:
        message = input("Enter message to send: ")
        client.send(message.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        print(f"Received from server: {response}")

if __name__ == "__main__":
    connect_to_server()