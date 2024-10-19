import pygame as pg
from input.user_input import Controller
from entities import Entity

def control_spectre(p: Entity, con: Controller):
    # WASD
    if con.w and con.w_s_prioirty:
        p.acc.y = p.acc_fac * -1
    elif con.s:
        p.acc.y = p.acc_fac
    if con.a and con.a_d_priority:
        p.acc.x = p.acc_fac * -1
    elif con.d:
        p.acc.x = p.acc_fac
    # Stop accelleration and decellerate
    if not con.w and not con.s:
        p.acc.y = 0
        p.vel.y *= p.dec_fac
    if not con.a and not con.d:
        p.acc.x = 0
        p.vel.x *= p.dec_fac
    # Zero vel if too very small
    if abs(p.vel.x) < 0.0001:
        p.vel.x = 0
    if abs(p.vel.y) < 0.0001:
        p.vel.y = 0

def control_gunner(p: Entity, con: Controller):
    # Left to Right
    if con.a and con.a_d_priority:
        p.acc.x = p.acc_fac * -1
    elif con.d:
        p.acc.x = p.acc_fac
    # Jump
    if con.eh.keydown(pg.K_SPACE) and p.can_jump:
        p.vel.y -= p.jump_force
        p.can_jump = False
    # Stop accelleration and decellerate
    if not con.a and not con.d:
        p.acc.x = 0
        p.vel.x *= p.dec_fac
    # Zero vel if too very small
    if abs(p.vel.x) < 0.0001:
        p.vel.x = 0
    if abs(p.vel.y) < 0.0001:
        p.vel.y = 0


    
