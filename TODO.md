IMMEDIATE:

- Devise structure for handling ONLINE and LOCAL game states, and switching between the two
- Devise how to define/utlize EntityHandler for both local and online entities






BACKLOG:

- Add in game ticks so differing frame rates have the same movement speed
- Add map making dev mode



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

