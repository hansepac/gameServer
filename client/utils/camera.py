import pygame as pg
from pygame import Vector2 as Vector
from utils.screen import get_entities_in_camera
from math import floor

class CameraBounds:
    def __init__(self, h: tuple, v: tuple):
        self.h: tuple = h
        self.v: tuple = v

class Camera():
    def __init__(self, anchor: Vector, scale: int = 20):
        """
        pos is center of where the camera is being rendered
        anchor is where the camera "wants" to be
        """
        self.anchor: Vector = anchor
        self.pos: Vector = anchor
        self.scale: int = scale
        window_surface = pg.display.get_surface()
        self.ww = window_surface.get_width()
        self.wh = window_surface.get_height()
        # Entites within camera bounds
        self.entities = []
        # Init Camera Bounds
        self.c_bound = CameraBounds(
            h = (-self.ww / self.scale, self.ww / self.scale),
            v = (-self.wh / self.scale, self.wh / self.scale)
        )

    def update_window_size(self):
        # Get window width and height
        window_surface = pg.display.get_surface()
        self.ww = window_surface.get_width()
        self.wh = window_surface.get_height()
    
    def update_camera_pos(self):
        self.pos = self.anchor

    def update_c_bound(self):
        # Relative distance from anchor center to horiz or vert camera bound
        rel_h_bound = self.ww / 2 / self.scale
        rel_v_bound = self.wh / 2 / self.scale
        # Update camera bounds
        self.c_bound.h = (self.anchor.x + rel_h_bound, self.anchor.x - rel_h_bound)
        self.c_bound.v = (self.anchor.x + rel_v_bound, self.anchor.x - rel_v_bound)

    # Not being used
    def get_entities(self, all_entities: list):
        self.entities = get_entities_in_camera(all_entities, self.c_bound.h, self.c_bound.v)

    def convert_to_screen(self, coords: tuple | Vector):
        x = (coords[0] - self.anchor.x) * self.scale + self.ww / 2
        y = (coords[1] - self.anchor.y) * self.scale + self.wh / 2
        return (int(floor(x)), int(floor(y)))

    def convert_to_game(self, coords: tuple | Vector):
        x = (coords[0] - self.ww / 2) / self.scale + self.anchor.x
        y = (coords[1] - self.wh / 2) / self.scale + self.anchor.y
        return (round(x, 3), round(y, 3))
