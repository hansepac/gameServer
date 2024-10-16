import socket
import threading
import json  # Import the JSON module
from pygame import Vector2 as Vector

class Client:
    address: tuple
    socket: socket.socket
    pos: tuple

class GameServer:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 12345
        self.clients = []

    def handle_client(self, client: Client):
        """Handle communication with the connected client."""
        print(f"New connection from {client.address}")
        self.clients.append(client)
        self.broadcast_new_client(client.address)

        try:
            while True:
                message = client.socket.recv(1024).decode('utf-8')
                if not message:
                    break
                
                # Update the player's position in the server
                client.pos = message.split(",")

                # Broadcast updated positions to all clients
                self.broadcast_positions()

        except Exception as e:
            print(f"Error handling client {client.address}: {e}")
        finally:
            # Cleanup
            self.broadcast_drop_client(client.address)
            print(f"Connection closed from {client.address}")
            client.socket.close()
            del client

    def broadcast_positions(self):
        """Send the current positions of all players to all clients."""
        client_pos = []  # Define the positions list here

        for client in self.clients:
            # addr is expected to be a tuple (IP address, port)
            client_info = {
                "address": client.address[0],
                "port": client.address[1],
                "pos.x": client.pos[0],
                "pos.y": client.pos[1]
            }
            client_pos.append(client_info)

        # Convert the list of positions to a JSON string
        msg = json.dumps({
            "msg_type": "pos",
            "dat": client_pos
        }) + "\n\n"
        
        for client in self.clients:
            try:
                client.socket.send(msg.encode('utf-8'))
            except Exception as e:
                print(f"Error sending to client: {e}")
                client.socket.close()
                self.clients.remove(client)
                del client
    
    def broadcast_new_client(self, address):
        msg = json.dumps({
            "msg_type": "new_client",
            "dat": {
                "address": address[0],
                "port": address[1]
            }
        }) + "\n\n"
        for client in self.clients:
            try:
                client.socket.send(msg.encode('utf-8'))
            except Exception as e:
                print(f"Error sending to client: {e}")
                client.socket.close()
                self.clients.remove(client)
                del client

    def broadcast_drop_client(self, address):
        msg = json.dumps({
            "msg_type": "drop_client",
            "dat": {
                "address": address[0],
                "port": address[1]
            }
        }) + "\n\n"
        for client in self.clients:
            try:
                client.socket.send(msg.encode('utf-8'))
            except Exception as e:
                print(f"Error sending to client: {e}")
                client.socket.close()
                self.clients.remove(client)
                del client

    def start_server(self):
        """Start the game server and listen for connections."""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen()
        print(f"Server started on {self.HOST}:{self.PORT}")

        while True:
            client_socket, client_address = server.accept()
            new_client = Client()
            new_client.address = client_address
            new_client.socket = client_socket
            new_client.pos = (0,0)
            thread = threading.Thread(target=self.handle_client, args=(new_client, ))
            thread.start()
            print(f"Active connections: {threading.activeCount() - 1}")

if __name__ == "__main__":
    server = GameServer()
    server.start_server()
