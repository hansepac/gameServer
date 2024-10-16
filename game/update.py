from __init__ import *
from entity.Circle import Circle
from server.client import send_server

def update():
    entityHandler.update_player()
    responses = send_server(client_socket, entityHandler.player)
    for response in responses:
        if response['msg_type'] == "pos":
            entityHandler.update_server_pos(response["dat"])
        elif response['msg_type'] == "new_client":
            print(f"NEW: {response['dat']}")
        elif response['msg_type'] == "drop_client":
            print(f"DROP: {response['dat']}")
            entityHandler.remove_player(response["dat"]["address"], response["dat"]["port"])