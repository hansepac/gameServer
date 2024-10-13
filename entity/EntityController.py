import pygame as pg
from __init__ import *
from entity.Circle import Circle
from input.user_input import Controller

con = Controller()

def control_circle(p: Circle):
    con.update()
    # WASD
    if con.w and con.w_s_prioirty:
        p.up = True
        p.down = False
    elif con.s:
        p.down = True
        p.up = False
    if con.a and con.a_d_priority:
        p.left = True
        p.right = False
    elif con.d:
        p.right = True
        p.left = False
    # Stop accelleration
    if not con.w and not con.s:
        p.up = p.down = False
    if not con.a and not con.d:
        p.left = p.right = False


    
