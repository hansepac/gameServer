from __init__ import *
from server.client import send_to_server
from server.update import update_from_server
import core.title as title
import core.game as game

def update():
    if gameState == gameState.TITLE:
        title.update()
    elif gameState == gameState.IN_GAME:
        game.update()