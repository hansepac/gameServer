from pygame import Vector2 as Vector
from input.user_input import Controller
from utils.Camera import Camera

def control_dead(p, con):
    pass

class Entity:
    def __init__(self,
            pos: Vector,
            vel: Vector = Vector(0,0),
            acc: Vector = Vector(0,0),
            size: float = 1,
            top_speed: int = 0.1,
            acc_fac: float = 0.1,
            dec_fac: float = 0.95
        ):
        self.pos: Vector = pos
        self.vel: Vector = vel
        self.acc: Vector = acc
        self.size: float = size
        self.top_speed: int = top_speed
        self.acc_fac: float = acc_fac
        self.dec_fac: int = dec_fac
        # Controller Function
        self.con_func: function = control_dead

    def update_vel(self, con: Controller):
        # Convert acc to vel
        self.vel += self.acc
        # Check for overshooting topspeed
        self.top_speed_limiter()

    def update_pos(self, camera: Camera):
        # Convert vel to pos
        self.pos += self.vel
        # If Hitbox, update hitbox
        if hasattr(self, "rect"):
            self.rect.topleft = camera.convert_to_screen(self.pos)

    def top_speed_limiter(self):
        if self.vel.length() > self.top_speed:
            self.vel.scale_to_length(self.top_speed)

