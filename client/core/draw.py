from __init__ import gameState
from entity.EntityController import control_circle
import title
import game

def draw():
    if gameState == gameState.TITLE:
        title.draw()
    elif gameState == gameState.IN_GAME:
        game.draw()
