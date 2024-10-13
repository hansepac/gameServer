import pygame as pg
from pygame import gfxdraw as dr
from pygame import Vector2 as Vector
from entity.update import *

class Entity:
    def __init__(self,
            pos: Vector,
            vel: Vector = Vector(0,0),
            acc: Vector = Vector(0,0),
            size: int = 30,
            top_speed: int = 5
        ):
        self.pos: Vector = pos
        self.vel: Vector = vel
        self.acc: Vector = acc
        self.size: int = size
        self.top_speed: int = top_speed

    def update_pos(self):
        update_pos_vel_acc(self.pos, self.vel, self.acc, self.top_speed)

