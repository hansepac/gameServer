from __init__ import entityHandler, onlineState, con, camera, mapHandler, col
from server.update import update_from_server

def update():
    # Update Camera
    camera.update_window_size()
    camera.scale = camera.ww / (mapHandler.width + 2)
    # Update Map Hitboxes
    mapHandler.update(camera)
    # Local vs Online
    if onlineState == onlineState.LOCAL:
        pass
    elif onlineState == onlineState.ONLINE:
        update_from_server()
    # Run Collisions
    col.entity_on_map(camera)
    # Update Player Controller
    entityHandler.control_player(con)
    # Update Entities
    entityHandler.update(con, camera)
    # Update Entity positions
    entityHandler.update_pos(con, camera)