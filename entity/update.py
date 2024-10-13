import pygame as pg
from pygame import Vector2 as Vector

def update_pos_vel_acc(pos: Vector, vel: Vector, acc: Vector, top_speed: float):
    # Convert acc to vel
    vel += acc
    # Check for overshooting topspeed
    if vel.length() > top_speed:
        vel.scale_to_length(top_speed)
    # Convert vel to pos
    pos += vel
    pos.x = int(round(pos.x))
    pos.y = int(round(pos.y))

def decelerate(entity, dec_fac: int = 0.9):
    """ dec_fac: int - Deccelleration Factor """
    # Come to a stop
    if abs(entity.vel.x) < 0.1:
        entity.vel.x = 0
    if abs(entity.vel.y) < 0.1:
        entity.vel.y = 0
    if not entity.up and not entity.down:
        entity.vel.y *= dec_fac
    if not entity.left and not entity.right:
        entity.vel.x *= dec_fac
        
