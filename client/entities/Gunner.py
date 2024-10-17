from pygame import gfxdraw as dr
from pygame import Vector2 as Vector
from entities.utils import decelerate
from entities.Entity import Entity
import pygame as pg

class Gunner(Entity):
    def __init__(self, pos: Vector):
        super().__init__(pos=pos)
        self.image = pg.Surface()
        
    def update(self):
        self.update_pos()

    def draw(self):
        dr.rectangle()