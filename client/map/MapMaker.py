import pygame as pg
from pygame import Vector2 as Vector
from collisions.hitboxes import RectHitbox
from math import floor

class Block():
    def __init__(self, pos: Vector, width: float = 1, height: float = 1):
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = RectHitbox(pos, width, height)
        self.color = (100, 100, 100)

class MapMaker:
    def __init__(self):
        self.grid = [[]]
        self.blocks = []
        self.width = 1
        self.height = 1

    def display_map(self):
        """Displays the grid in a human-readable format."""
        for row in self.grid:
            print(" ".join(["." if cell is None else str(cell) for cell in row]))
        print()
    
    def create_blocks(self):
        # "X" represents a block
        b = "X"
        # Get indecies of max border
        grid_h_idx = len(self.grid) - 1
        grid_w_idx = len(self.grid[0]) - 1
        for j, row in enumerate(self.grid):
            for i, item in enumerate(row):
                if item == b:
                    # Create Block
                    block = Block(pos = Vector(i, j))
                    # HORIZONTAL CHECKS
                    if i != 0:
                        if i == grid_w_idx:
                            block.rect.r = False
                        if row[i - 1] == b:
                            block.rect.l = False
                    if i != grid_w_idx:
                        if i == 0:
                            block.rect.l = False
                        if row[i + 1] == b:
                            block.rect.r = False
                    # VERTICAL CHECKS
                    if j != 0:
                        if j == grid_h_idx:
                            block.rect.b = False
                        if self.grid[j - 1][i] == b:
                            block.rect.l = False
                    if j != grid_h_idx:
                        if j == 0:
                            block.rect.t = False
                        if self.grid[j + 1][i] == b:
                            block.rect.r = False
                    self.blocks.append(block)
        self.create_border_blocks()

    def create_border_blocks(self):
        border_blocks = [
            # Top
            Block(Vector(0, -1), self.width, 1),
            # Right
            Block(Vector(self.width, 0), 1, self.height),
            # Bottom
            Block(Vector(0, self.height), self.width, 1),
            # Left
            Block(Vector(-1, 0), 1, self.height)
        ]
        self.blocks += border_blocks
        
    def empty_map(self, width: int, height: int):
        self.width = width
        self.height = height
        self.center = Vector(self.width / 2, self.height / 2)
        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]

    def basic_map(self, width: int = 20, height: int = 10):
        # Init
        self.empty_map(width, height)
        # Add Floor
        bottom_row_idx = self.height - 1
        for i in range(self.width):
            self.grid[bottom_row_idx][i] = "X"
        # Add two platforms
        half_way_idx = floor(self.height / 2) - 1
        for i in range(floor(self.width / 3)):
            self.grid[half_way_idx][i] = "X"
            self.grid[half_way_idx][(self.width-1) - i] = "X"
        return self.grid