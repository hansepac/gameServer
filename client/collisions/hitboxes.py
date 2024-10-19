import pygame as pg
from pygame import Vector2 as Vector

class RectHitbox(pg.Rect):
    def __init__(self, pos: Vector, width: float, height: float):
        super().__init__(pos.x, pos.y, width, height)
        self.color = (100, 100, 100)
        # Collision for that side active
        self.t: bool = True
        self.r: bool = True
        self.b: bool = True
        self.l: bool = True

class CircHitbox:
    def __init__(self, pos: Vector, size: float = 0.5):
        self.pos: Vector = pos
        self.size: float = size