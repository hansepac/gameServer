from entities.Entity import Entity

class Player:
    def __init__(self,
            address: tuple | None = None,
            entity: Entity | None = None
        ):
        self.address = address
        self.entity = entity