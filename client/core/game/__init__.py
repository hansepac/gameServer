from .draw import draw
from .update import update

from __init__ import entityHandler, player
from entities.Circle import Circle
from pygame import Vector2 as Vector

def game_init():
    player_entity = Circle(Vector(0,0))
    player.entity = player_entity
    entityHandler.entities.append(player_entity)
    entityHandler.players[player.address] = player