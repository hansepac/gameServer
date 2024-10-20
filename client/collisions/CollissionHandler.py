from pygame import Vector2 as Vector
from pygame import gfxdraw as dr
from entities.EntityHandler import EntityHandler
from map.MapHandler import MapHandler
from utils.Camera import Camera
from entities.Gunner import Gunner
from .collision_functions import gunner_on_block, rect_on_rect, ERROR
from .hitboxes import RectHitbox
from map.MapMaker import Block
from math import ceil

class CollissionHandler:
    def __init__(self, entH: EntityHandler, mapH: MapHandler, cam: Camera):
        self.entH = entH
        self.mapH = mapH
        self.cam = cam
    
    # Entities on Entities
    def entity_on_entity(self):
        pass

    # Entities on Map
    def entity_on_map(self, camera: Camera):
        block: Block
        for entity in self.entH.entities:
            # Disable jumping until block is hit
            checks_list = self.incremental_checks(entity.pos, entity.vel, col_error=ERROR*2)
            for inc_pos in checks_list:
                print(f"{len(checks_list)}, {inc_pos} {entity.rect.topleft}")
                for block in self.mapH.blocks:
                    if isinstance(entity, Gunner):
                        entity.rect.topleft = inc_pos
                        col = rect_on_rect(entity.rect, block.rect)
                        if col:
                            gunner_on_block(col, entity, block, camera)

    def player_on_map(self, camera: Camera):
        player_ent: Gunner = self.entH.player.entity
        block: Block
        # Set jump to false until collission
        player_ent.can_jump = False
        for block in self.mapH.blocks:
            if isinstance(player_ent, Gunner):
                col = rect_on_rect(player_ent.rect, block.rect)
                if col:
                    gunner_on_block(col, player_ent, block, camera)
    
    def draw_hitboxes(self, window, color = (0, 255, 0)):
        block: Block
        for block in self.mapH.blocks:
            self.draw_rect_hitbox(window, block.rect)
        for entity in self.entH.entities:
            self.draw_rect_hitbox(window, entity.rect)
            
    def draw_rect_hitbox(self, window, r: RectHitbox, color = (0, 255, 0)):
        if r.t:
            dr.line(window, r.left, r.top+1, r.right-1, r.top+1, color)
        if r.r:
            dr.line(window, r.right-2, r.top, r.right-2, r.bottom-1, color)
        if r.b:
            dr.line(window, r.right-1, r.bottom-2, r.left, r.bottom-2, color)
        if r.l:
            dr.line(window, r.left+1, r.bottom-1, r.left+1, r.top, color)

    def incremental_checks(self, pos: Vector, vel: Vector, col_error: int):
        """Returns list of checks needed when vel is too high"""
        screen_vel = self.cam.scale * vel
        pixels_to_be_moved = max(screen_vel[0], screen_vel[1])
        num_checks = ceil(pixels_to_be_moved / col_error)
        # If velocity is not sufficient to break error range
        if num_checks < 1:
            return [pos]
        nudged_pos = []
        for step in range(num_checks):
            step_pos = pos + vel * (step / num_checks)
            screen_pos = self.cam.convert_to_screen(step_pos)
            nudged_pos.append(screen_pos)
        return nudged_pos
