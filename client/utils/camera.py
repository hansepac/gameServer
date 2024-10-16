import pygame as pg
from pygame import Vector2 as Vector
from utils.screen import get_entities_in_camera
from __init__ import *

class CameraBounds:
    h: tuple
    v: tuple

class Camera():
    def __init__(self, anchor: Vector, scale: int):
        """
        pos is center of where the camera is being rendered
        anchor is where the camera "wants" to bee
        """
        self.anchor: Vector = anchor
        self.pos: Vector = anchor
        self.scale: int = scale
        self.entities: list = []
        self.ww = WINDOW_WIDTH
        self.wh = WINDOW_HEIGHT
        self.c_bound: CameraBounds
        self.c_bound.h = (-10, 10)
        self.c_bound.v = (-10, 10)

    def update_window_size(self):
        # Get window width and height
        window_surface = pg.display.get_surface()
        self.window_width = window_surface.get_width()
        self.window_height = window_surface.get_height()
    
    def update_camera_pos(self):
        self.pos = self.anchor

    def update_c_bound(self):
        # Relative distance from anchor center to horiz or vert camera bound
        rel_h_bound = self.ww / 2 / self.scale
        rel_v_bound = self.wh / 2 / self.scale
        # Update camera bounds
        self.c_bound.h = (self.anchor.x + rel_h_bound, self.anchor.x - rel_h_bound)
        self.c_bound.v = (self.anchor.x + rel_v_bound, self.anchor.x - rel_v_bound)

    def get_entities(self, all_entities: list):
        self.entities = get_entities_in_camera(all_entities, self.c_bound.h, self.c_bound.v)

    def draw_entities(self):
        pass
