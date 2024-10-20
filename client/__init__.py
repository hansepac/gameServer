import os
os.chdir(os.path.dirname(__file__))

# WINDOW SETUP
import pygame as pg
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT), pg.RESIZABLE, vsync=1)
pg.display.set_caption('Stick Fight')
pg.display.init()
pg.init()

DEV = True

# SERVER SETUP
from dotenv import load_dotenv
if DEV:
    load_dotenv(".env.dev")
else:
    load_dotenv(".env.prod")

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

# CONNECTING TO SERVER
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
local_address = client_socket.getsockname()

from entities.Player import Player
player = Player(local_address)

# GAME SETUP
FRAME_RATE = 60
CAMERA_SCALE = 60

# Game States
from utils.states import GameState, OnlineState
gameState = GameState(1) # {0: TITLE, 1: IN_GAME}
onlineState = OnlineState(1) # {0: LOCAL, 1: ONLINE}

# EntityHandler
from entities import EntityHandler
entityHandler = EntityHandler(player)

# Camera
from utils.Camera import Camera
from pygame import Vector2 as Vector
camera = Camera(Vector(0,0), scale = CAMERA_SCALE)

# Map
from map.MapHandler import MapHandler
mapHandler = MapHandler(Vector(0,0))

# Controller
from entities.entity_controllers import Controller
con = Controller()

# Collisions
from collisions.CollissionHandler import CollissionHandler
col = CollissionHandler(entityHandler, mapHandler, camera)