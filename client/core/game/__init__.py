from .draw import draw
from .update import update

from __init__ import entityHandler, player, camera, mapHandler
from entities.Circle import Circle
from entities.Gunner import Gunner
from pygame import Vector2 as Vector

def game_init():
    # Create Map
    mapHandler.basic_map()
    # Create Player Entity
    player_entity = Gunner(mapHandler.center)
    # Update Player with entity
    player.entity = player_entity
    # Update entityHandler with player and player_entity
    entityHandler.entities.append(player_entity)
    entityHandler.players[player.address] = player
    # Center Camera on center of map
    camera.anchor = mapHandler.center