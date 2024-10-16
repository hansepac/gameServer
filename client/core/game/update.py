from __init__ import entityHandler, onlineState
from server.update import update_from_server

def update():
    if onlineState == onlineState.LOCAL:
        pass
    elif onlineState == onlineState.ONLINE:
        try:
            update_from_server()
        except:
            print("Error with server")

    entityHandler.update_player()