import pygame as pg
from .hitboxes import RectHitbox, CircHitbox
from entities.Gunner import Gunner
from map.MapMaker import Block
from utils.Camera import Camera

ERROR = 5

# GENERAL COLLISIONS
def circle_on_rect(c: CircHitbox, r: RectHitbox):
    pass

def circle_on_circle(c1: CircHitbox, c2: CircHitbox):
    return (c1.pos - c2.pos).length() <= c1.size + c2.size

def rect_on_rect(r1: RectHitbox, r2: RectHitbox):
    collisions = {"t": False, "r": False, "b": False, "l": False}
    if (r1.bottom >= (r2.top - ERROR) and r1.bottom <= (r2.top + ERROR)) and (r1.b and r2.t) and not (r1.left >= r2.right or r1.right <= r2.left):
        collisions["b"] = True
    elif (r1.top >= (r2.bottom - ERROR) and r1.top <= (r2.bottom + ERROR)) and (r1.t and r2.b) and not (r1.left >= r2.right or r1.right <= r2.left):
        collisions["t"] = True
    if (r1.right >= (r2.left - ERROR) and r1.right <= (r2.left + ERROR)) and (r1.r and r2.l) and not (r1.top >= r2.bottom or r1.bottom <= r2.top):
        collisions["r"] = True
    elif (r1.left >= (r2.right - ERROR) and r1.left <= (r2.right + ERROR)) and (r1.l and r2.r) and not (r1.top >= r2.bottom or r1.bottom <= r2.top):
        collisions["l"] = True
    if collisions.values() == [False, False, False, False]:
        return False
    else:
        return collisions

# CLASS COLLISIONS
def gunner_on_block(col, g: Gunner, b: Block, camera: Camera):
    # Check for Collisions
    if col["t"]:
        if g.vel.y < 0:
            g.rect.top = b.rect.bottom
            g.pos.y = camera.convert_to_game((0, g.rect.top))[1]
            g.vel.y = 0
    elif col["b"]:
        g.can_jump = True
        if g.vel.y > 0:
            g.rect.bottom = b.rect.top
            g.pos.y = camera.convert_to_game((0, g.rect.bottom - g.rect.height))[1]
            g.vel.y = 0
    if col["r"]:
        if g.vel.x > 0:
            g.rect.right = b.rect.left
            g.pos.x = camera.convert_to_game((g.rect.right - g.rect.width, 0))[0]
            g.vel.x = 0
    elif col["l"]:
        if g.vel.x < 0:
            g.rect.left = b.rect.right
            g.pos.x = camera.convert_to_game((g.rect.left, 0))[0]
            g.vel.x = 0

    