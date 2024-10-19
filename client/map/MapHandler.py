import pygame as pg
from pygame import gfxdraw as dr
from pygame import Vector2 as Vector
from utils.Camera import Camera
from map.MapMaker import MapMaker
from map.MapMaker import Block
from math import floor

class MapHandler(MapMaker):
    def __init__(self, corner: Vector = Vector(0,0), width: int = 20, height: int = 10):
        super().__init__()
        self.width = width
        self.height = height
        # In game coordinate to the top left corner of the map
        self.corner = corner
        self.center = Vector(
            self.corner.x + self.width / 2,
            self.corner.y + self.height / 2
        )
        self.basic_map()
        self.create_blocks()

    def update(self, camera: Camera):
        block: Block
        for block in self.blocks:
            block.rect.topleft = camera.convert_to_screen(block.pos)
            block.rect.width = int(floor(camera.scale * block.width))
            block.rect.height = int(floor(camera.scale * block.height))
    
    def draw(self, window, camera: Camera):
        for j, row in enumerate(self.grid):
            for i, item in enumerate(row):
                if item == "X":
                    (x, y) = camera.convert_to_screen((i, j))
                    dr.rectangle(
                        window,
                        pg.Rect(x, y, camera.scale, camera.scale),
                        (100, 100, 100)
                    )

    def draw_border(self, window, camera: Camera, color = (255, 0, 0)):
        color = color
        tl = camera.convert_to_screen(Vector(self.corner.x, self.corner.y))
        tr = camera.convert_to_screen(Vector(self.corner.x + self.width, self.corner.y))
        br = camera.convert_to_screen(Vector(self.corner.x + self.width, self.corner.y + self.height))
        bl = camera.convert_to_screen(Vector(self.corner.x, self.corner.y + self.height))
        # Top
        dr.line(window, tl[0], tl[1], tr[0], tr[1], color)
        # Right
        dr.line(window, tr[0] - 1, tr[1], br[0] - 1, br[1], color)
        # Bottom
        dr.line(window, br[0], br[1], bl[0], bl[1], color)
        # Top
        dr.line(window, bl[0], bl[1], tl[0], tl[1], color)