from .update import update
from .draw import draw

from __init__ import entityHandler, local_address, local_port
from entity.Circle import Circle
from pygame import Vector2 as Vector

def game_init():
    player_entity = Circle(Vector(0,0))
    entityHandler.add_player(local_address, local_port, player_entity)