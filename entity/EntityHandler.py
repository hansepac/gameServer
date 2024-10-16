import pygame as pg
from pygame import Vector2 as Vector
from entity.Entity import Entity
from entity.Player import Player
from entity.Circle import Circle
from entity.EntityController import control_circle

class EntityHandler:
    def __init__(self):
        self.entities = []
        self.players: dict[Player] = {}
        self.player: Entity = Circle(Vector(0,0))

    def collisions(self):
        pass

    def update_player(self):
        control_circle(self.player)
        if self.player:
            self.player.update()

    def update_server_pos(self, dat):
        for client_dat in dat:
            # Extract data
            address = client_dat["address"]
            port = str(client_dat["port"])
            # Create Client_id (Address:Port)
            client_id = address + ":" + port
            try:
                x_pos = float(client_dat["pos.x"])
                y_pos = float(client_dat["pos.y"])
            except ValueError:
                if client_id in self.players:
                    x_pos = self.players[client_id].entity.pos.x
                    y_pos = self.players[client_id].entity.pos.y
                else:
                    x_pos = y_pos = 0

            # Check if client is registered locally
            if not client_id in self.players:
                # Register new client
                self.add_player(address, port, Circle(Vector(x_pos, y_pos)))
            else:
                # Update local position
                self.players[client_id].entity.pos = Vector(x_pos, y_pos)
            
    def update(self):
        for entity in self.entities:
            entity.update()

    def draw(self, window):
        for entity in self.entities:
            entity.draw(window)

    def add_player(self, address: str, port: int, entity: Entity):
        # Create Player Class
        new_player = Player()
        new_player.address = address
        new_player.port = port
        new_player.entity = entity
        new_player.id = address + ":" + str(port)
        
        # Add to players
        self.players[new_player.id] = new_player

        # Add to Entities
        self.entities.append(entity)

    def remove_player(self, address: str, port: int):
        player_id = address + ":" + str(port)
        player = self.players[player_id]
        self.entities.remove(player.entity)
        del self.players[player_id]

