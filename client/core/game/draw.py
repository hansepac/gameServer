from __init__ import window, entityHandler
from entity.EntityController import control_circle

def draw():
    # Clear Screen
    window.fill((0,0,0))
    entityHandler.draw(window)