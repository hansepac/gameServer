from pygame import Vector2 as Vector
from entities import Entity, Player, Circle
from entities.entity_controllers import control_spectre
from input.user_input import Controller
from utils.Camera import Camera



class EntityHandler:
    def __init__(self, player: Player):
        self.player: Player = player
        self.entities = []
        self.players: dict[Player] = {}

    def control_player(self, con: Controller):
        if self.player:
            self.player.entity.control(con)

    def update_server_pos(self, dat):
        for client_dat in dat:
            # Extract data
            address = tuple(client_dat["address"])
            try:
                x_pos = float(client_dat["pos.x"])
                y_pos = float(client_dat["pos.y"])
            except ValueError:
                if address == self.player.address:
                    pass
                elif address in self.players:
                    x_pos = self.players[address].entity.pos.x
                    y_pos = self.players[address].entity.pos.y
                else:
                    x_pos = y_pos = 0

            # Check if client is registered locally
            if not address in self.players:
                # Register new client
                self.add_player(address, Circle(Vector(x_pos, y_pos)))
            else:
                # Update local position
                self.players[address].entity.pos = Vector(x_pos, y_pos)
            
    def update(self, camera: Camera, con: Controller):
        for entity in self.entities:
            entity.update(camera, con)

    def update_pos(self, con: Controller, camera: Camera):
        entity: Entity
        for entity in self.entities:
            entity.update_pos(camera)

    def draw(self, window, camera: Camera):
        for entity in self.entities:
            entity.draw(window, camera)

    def add_player(self, address: tuple, entity: Entity):
        # Create Player Class
        new_player = Player(address, entity)
        # Add to players
        self.players[new_player.address] = new_player
        # Add to Entities
        self.entities.append(entity)

    def remove_player(self, address: tuple):
        player: Player = self.players[address]
        self.entities.remove(player.entity)
        del self.players[address]

