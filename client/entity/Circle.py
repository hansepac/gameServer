from pygame import gfxdraw as dr
from pygame import Vector2 as Vector
from entity.utils import decelerate
from entity import Entity

class Circle(Entity):
    def __init__(self, pos: Vector):
        super().__init__(pos=pos)
        self.dec: bool = True
        self.dec_fac: int = 0.9
        self.up: bool = False
        self.down: bool = False
        self.left: bool = False
        self.right: bool = False
        self.l_r_lock: bool = False
        self.u_d_lock: bool = False
        self.acc_fac: int = 0.5

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

        decelerate(self, 0.9)
        
        self.update_pos()

    def draw(self, window):
        x = int(self.pos.x)
        y = int(self.pos.y)
        dr.filled_circle(window, x, y, self.size, (255, 255, 0))

