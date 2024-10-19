import pygame as pg
from input.EventHandler import EventHandler

eventHandler = EventHandler()

def game_end_check():
    """Ends game if escape is pressed or if the window is closed"""
    eventHandler.poll_events()
    for event in eventHandler.events:
        if event.type == pg.QUIT or eventHandler.keydown(pg.K_ESCAPE):
            return False
    return True

class Controller:
    def __init__(self):
        # EventHandler
        self.eh: EventHandler = eventHandler
        self.w: bool = False
        self.a: bool = False
        self.s: bool = False
        self.d: bool = False
        # True if A is prioritized
        self.a_d_priority: bool = False
        # True if W is prioritized
        self.w_s_prioirty: bool = False
        self.mouse_pos = 0

    def update(self):
        # WASD
        if self.eh.keydown(pg.K_w):
            self.w = True
            self.w_s_prioirty = True
        if self.eh.keyup(pg.K_w):
            self.w = False
            self.w_s_prioirty = False
        if self.eh.keydown(pg.K_s):
            self.s = True
            self.w_s_prioirty = False
        if self.eh.keyup(pg.K_s):
            self.s = False
            self.w_s_prioirty = True
        if self.eh.keydown(pg.K_a):
            self.a = True
            self.a_d_priority = True
        if self.eh.keyup(pg.K_a):
            self.a = False
            self.a_d_priority = False
        if self.eh.keydown(pg.K_d):
            self.d = True
            self.a_d_priority = False
        if self.eh.keyup(pg.K_d):
            self.d = False
            self.a_d_priority = True

        # GET MOUSE POS
        self.mouse_pos = pg.mouse.get_pos()