import socket
import pygame as pg

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
FRAME_RATE = 100

CAMERA_SCALE = 10

# Networking setup
HOST = '127.0.0.1'
PORT = 12345

# Connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
local_address, local_port = client_socket.getsockname()

window = pg.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT),  vsync=1)
pg.display.set_caption('Platformer')
pg.display.init()
pg.init()

from entity.EntityHandler import EntityHandler
entityHandler = EntityHandler()