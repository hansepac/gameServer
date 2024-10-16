# WINDOW SETUP
import pygame as pg
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),  vsync=1)
pg.display.set_caption('Platformer')
pg.display.init()
pg.init()

# SERVER SETUP
from dotenv import load_dotenv
import os
load_dotenv()
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

# CONNECTING TO SERVER
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
local_address, local_port = client_socket.getsockname()

# GAME SETUP
FRAME_RATE = 100
CAMERA_SCALE = 10

from core.states import GameState, OnlineState
gameState = GameState(1) # {0: TITLE, 1: IN_GAME}
onlineState = OnlineState(1) # {0: LOCAL, 1: ONLINE}

from entity import EntityHandler
entityHandler = EntityHandler()

from input import EventHandler
eventHandler = EventHandler()