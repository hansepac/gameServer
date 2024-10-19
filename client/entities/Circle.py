from pygame import gfxdraw as dr
from pygame import Vector2 as Vector
from entities.Entity import Entity
from entities.entity_controllers import control_spectre
from input.user_input import Controller
from utils.Camera import Camera
from math import floor

class Circle(Entity):
    def __init__(self, pos: Vector):
        super().__init__(pos=pos)
        self.con_func: function = control_spectre

    def update(self, con: Controller):
        self.update_pos(con)

    def draw(self, window, camera: Camera):
        pos: Vector = Vector(camera.convert_to_screen(self.pos))
        size: int = floor(self.size * camera.scale / 2)
        dr.filled_circle(window, round(pos.x), round(pos.y), size, (255, 255, 0))

