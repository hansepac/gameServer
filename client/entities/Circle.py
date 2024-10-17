from pygame import gfxdraw as dr
from pygame import Vector2 as Vector
from entities.utils import decelerate
from entities.Entity import Entity
from utils.Camera import Camera
from math import floor

class Circle(Entity):
    def __init__(self, pos: Vector):
        super().__init__(pos=pos)
        self.dec: bool = True
        self.dec_fac: int = 0.90
        self.up: bool = False
        self.down: bool = False
        self.left: bool = False
        self.right: bool = False
        self.l_r_lock: bool = False
        self.u_d_lock: bool = False
        self.acc_fac: int = 0.1

    def update(self):
        if self.up:
            self.acc.y = self.acc_fac * -1
        if self.down:
            self.acc.y = self.acc_fac
        if self.left:
            self.acc.x = self.acc_fac * -1
        if self.right:
            self.acc.x = self.acc_fac
        if not self.up and not self.down:
            self.acc.y = 0
        if not self.left and not self.right:
            self.acc.x = 0

        decelerate(self, self.dec_fac)
        
        self.update_pos()

    def draw(self, window, camera: Camera):
        pos: tuple = camera.convert_to_screen(self.pos)
        size: int = floor(self.size * camera.scale)
        dr.filled_circle(window, pos[0], pos[1], size, (255, 255, 0))

