from __init__ import window, entityHandler, camera, mapHandler, col
from pygame import gfxdraw as dr
import pygame as pg

def draw():
    # Clear Screen
    window.fill((0,0,0))
    # Draw Map
    mapHandler.draw(window, camera)
    #mapHandler.draw_border(window, camera)
    #col.draw_hitboxes(window)
    # Draw entities
    entityHandler.draw(window, camera)