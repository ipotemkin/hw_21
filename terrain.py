from unit import Unit


class Terrain:
    def __init__(self, terrain, walkable):
        self.terrain = terrain  # name of the terrain
        self.walkable = walkable

    def is_walkable(self):
        return self.walkable

    def get_terrain(self):
        return self.terrain

    def step_on(self, obj: Unit):
        pass


class Grass(Terrain):
    def __init__(self):
        super().__init__(terrain="Grass", walkable=True)


class Wall(Terrain):
    def __init__(self):
        super().__init__(terrain="Wall", walkable=False)


class Door(Terrain):
    def __init__(self):
        super().__init__(terrain="Door", walkable=False)

    def step_on(self, obj: Unit):
        if obj.has_key_():
            obj.set_escaped()
            self.walkable = True


class Key(Terrain):
    def __init__(self):
        super().__init__(terrain="Key", walkable=True)

    def step_on(self, obj: Unit):
        obj.set_key()


class Trap(Terrain):
    def __init__(self, damage=10):
        super().__init__(terrain="Trap", walkable=True)
        self.damage = damage

    def step_on(self, obj: Unit):
        obj.get_damage(self.damage)
