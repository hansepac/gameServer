from __init__ import *
import pygame as pg
from input.user_input import game_end_check
from game import game_init, update, draw

# INITIALIZE FRAME RATE STUFF
delta_time = 0.0
clock = pg.time.Clock()

# GAME LOOP
game_init()
game_running = True

while game_running:
    # Check if window "X" is pressed, or ESC
    game_running = game_end_check()
    # UPDATE ITEMS
    update()
    # DRAW SCREEN
    draw()
    # UPDATE DISPLAY
    pg.display.update()
    delta_time = 0.001 * clock.tick(FRAME_RATE)

# Cleanup and close
client_socket.close()
pg.quit()