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
        # Horizontal Movement
        self.acc_fac = 0.01
        self.dec_fac = 0.90
        self.top_speed_walk: bool = 0.08
        self.drag = 0.2
        # Vertical
        self.can_jump: bool = False
        self.top_speed: bool = 0.5
        self.term_vel: bool = 0.2
        self.jump_force: float = 0.3
        self.gravity: float = 0.02
        # Controller
        self.con_func = control_gunner

    def update(self, con: Controller, camera: Camera):
        # Update hitbox
        pos: tuple = camera.convert_to_screen(self.pos)
        self.rect.topleft = pos
        self.rect.width = floor(self.width * camera.scale)
        self.rect.height = floor(self.height * camera.scale)
        # Update Gravity
        if self.can_jump == False:
            self.vel.y += self.gravity
        self.update_vel(con)

    def control(self, con: Controller):
        self.con_func(self, con)

    def draw(self, window, camera: Camera):
        pos: tuple = camera.convert_to_screen(self.pos)
        size: int = floor(self.size * camera.scale)
        width = size / 2
        height = size
        rect = pg.Rect(pos[0], pos[1], width, height)
        dr.rectangle(window, rect, self.color)
    
    def top_speed_limiter(self):
        if self.vel.x:
            horiz_dir = abs(self.vel.x) / self.vel.x
        else:
            horiz_dir = 0
        # Walking Speed
        if abs(self.vel.x) > self.top_speed:
            self.vel.x = self.top_speed * horiz_dir
        else:
            # Walk Resistance
            if abs(self.vel.x) > self.top_speed_walk and self.can_jump:
                self.vel.x = self.top_speed_walk * horiz_dir
            # Drag
            if not self.can_jump:
                drag = self.drag * self.vel.x ** 2
                self.vel.x = self.vel.x - drag * horiz_dir
            # Terminal Velocity
            if self.vel.y > self.term_vel:
                self.vel.y = self.term_vel