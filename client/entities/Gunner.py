import pygame as pg
from pygame import gfxdraw as dr
from pygame import Vector2 as Vector
from entities.Entity import Entity
from entities.entity_controllers import control_spectre, control_gunner
from collisions.hitboxes import RectHitbox
from input.user_input import Controller
from math import floor
from utils.Camera import Camera

class Gunner(Entity):
    def __init__(self, pos: Vector):
        Entity.__init__(self, pos=pos)
        # Hitbox
        self.width = self.size / 2
        self.height = self.size
        self.rect = RectHitbox(pos=pos, width=10, height=20)
        # Visual
        self.color = (255, 255, 0)
        # Movement
        self.acc_fac = 0.01
        self.dec_fac = 0.90
        #   Vertical
        self.can_jump: bool = False
        self.top_speed: bool = 0.5
        self.term_vel: bool = 0.2
        self.jump_force: float = 0.4
        self.gravity: float = 0.02
        #   Horizontal
        self.top_speed_walk: bool = 0.07
        # Controller
        self.con_func = control_gunner

    def update(self, con: Controller, camera: Camera):
        # Update hitbox
        pos: tuple = camera.convert_to_screen(self.pos)
        self.rect.topleft = pos
        self.rect.width = floor(self.width * camera.scale)
        self.rect.height = floor(self.height * camera.scale)
        # acc -> vel, and cap vel
        self.update_vel(con)

    def control(self, con: Controller):
        self.con_func(self, con)

    def update_pos(self, con: Controller, camera):
        # Update gravity
        if self.can_jump == False:
            self.vel.y += self.gravity
        super().update_pos(camera)

    def draw(self, window, camera: Camera):
        pos: tuple = camera.convert_to_screen(self.pos)
        size: int = floor(self.size * camera.scale)
        width = size / 2
        height = size
        rect = pg.Rect(pos[0], pos[1], width, height)
        dr.rectangle(window, rect, self.color)
    
    def top_speed_limiter(self):
        # Walking Speed
        if abs(self.vel.x) > self.top_speed:
            self.vel.x = self.top_speed * (self.vel.x / abs(self.vel.x))
        else:
            if abs(self.vel.x) > self.top_speed_walk and self.can_jump:
                self.vel.x = self.top_speed_walk * (self.vel.x / abs(self.vel.x))
            if self.vel.y > self.term_vel:
                self.vel.y = self.term_vel