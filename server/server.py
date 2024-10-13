import socket
import threading
import json  # Import the JSON module

class GameServer:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 12345
        self.clients = []
        self.client_positions = {}  # To track client positions

    def handle_client(self, client_socket: socket.socket, address):
        """Handle communication with the connected client."""
        print(f"New connection from {address}")
        self.clients.append(client_socket)
        self.broadcast_new_client(address[0], address[1])

        try:
            while True:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                
                # Update the player's position in the server
                self.client_positions[address] = message.split(",")

                # Broadcast updated positions to all clients
                self.broadcast_positions()

        except Exception as e:
            print(f"Error handling client {address}: {e}")
        finally:
            # Cleanup
            self.broadcast_drop_client(address[0], address[1])
            client_socket.close()
            self.clients.remove(client_socket)
            del self.client_positions[address]
            print(f"Connection closed from {address}")

    def broadcast_positions(self):
        """Send the current positions of all players to all clients."""
        client_pos = []  # Define the positions list here

        for addr, pos in self.client_positions.items():
            # addr is expected to be a tuple (IP address, port)
            client_info = {
                "address": addr[0],
                "port": addr[1],
                "pos.x": pos[0],
                "pos.y": pos[1]
            }
            client_pos.append(client_info)

        # Convert the list of positions to a JSON string
        msg = json.dumps({
            "msg_type": "pos",
            "dat": client_pos
        }) + "\n\n"
        
        for client in self.clients:
            try:
                client.send(msg.encode('utf-8'))
            except Exception as e:
                print(f"Error sending to client: {e}")
                client.close()
                self.clients.remove(client)
    
    def broadcast_new_client(self, address, port):
        msg = json.dumps({
            "msg_type": "new_client",
            "dat": {
                "address": address,
                "port": port
            }
        }) + "\n\n"
        for client in self.clients:
            try:
                client.send(msg.encode('utf-8'))
            except Exception as e:
                print(f"Error sending to client: {e}")
                client.close()
                self.clients.remove(client)

    def broadcast_drop_client(self, address, port):
        msg = json.dumps({
            "msg_type": "drop_client",
            "dat": {
                "address": address,
                "port": port
            }
        }) + "\n\n"
        for client in self.clients:
            try:
                client.send(msg.encode('utf-8'))
            except Exception as e:
                print(f"Error sending to client: {e}")
                client.close()
                self.clients.remove(client)

    def start_server(self):
        """Start the game server and listen for connections."""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.HOST, self.PORT))
        server.listen()
        print(f"Server started on {self.HOST}:{self.PORT}")

        while True:
            client_socket, client_address = server.accept()
            thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
            thread.start()
            print(f"Active connections: {threading.activeCount() - 1}")

if __name__ == "__main__":
    server = GameServer()
    server.start_server()
