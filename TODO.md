IMMEDIATE:





BACKLOG:

- Add in game ticks so differing frame rates have the same movement speed
- Add map making dev mode


PHYSICS PEMDAS:

- Update Map hitboxes
- Update positions from server
- Run collisions
- Gunner Update:
    - Update hitbox screen rect
    - Contorller
    - Add acc to vel
    - Cap vel
- Entities:
    - Update pos with vel
- Gunner:
    - Add gravity


MOVING PARTS:
- Entity Handler
    - Stores entity objects
        - Including item objects
    - Updates all objects
    - Handles Collisisons
        - Gets collisions
        - Use collision functions:
            player_bullet(p: Player, b: Bullet)
            player_floor(p: Player, f: Floor)
            player_slope(p:...)
            player_gun(p:...)

- Collision Handler
    - 

- Map Handler
    - Stores info for map objects / locations
    - Controls map if parts move? maybe
    - Draws map

- UI Handler
    - layer above Map Handler
    - 

- Map Objects
    - Structure
        - Blocks
        - Slopes?
    - Hazards
        - Spikey
        - Lava



GAMEPLAY IDEAS:
- You get one movement ability at start
    - Dodge
    - Portal Gun
    - Grapple Hook


SERVER HANDLING:
- Game updates objects when server doesn't send info about them

