class UnitDied(Exception):
    pass


class Unit:
    def __init__(self, coord, hp=100, got_key=False, escaped=False):
        self.hp = hp
        self.got_key = got_key
        self.coord = coord
        self.escaped = escaped

    def get_coordinates(self):
        return self.coord

    def set_coordinates(self, x, y):
        self.coord = [x, y]

    def get_hp(self):
        return self.hp

    def set_hp(self, new_value):
        self.hp = new_value

    def set_damage(self, value):
        self.hp -= value

    def has_key_(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def has_escaped(self):
        return self.escaped

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        self.hp -= damage
        if not self.is_alive():
            raise UnitDied

    def has_position(self, x, y):
        return self.get_coordinates() == [x, y]

    def set_escaped(self):
        self.escaped = True


class Ghost(Unit):
    def __init__(self, coord, hp):
        super().__init__(coord, hp)
        self.name = "Ghost"
