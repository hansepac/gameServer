from __init__ import window, entityHandler, camera
from entities.EntityController import control_circle
from pygame import gfxdraw as dr
import pygame as pg

def draw():
    # Clear Screen
    window.fill((0,0,0))
    entityHandler.draw(window, camera)