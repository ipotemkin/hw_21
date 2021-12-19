from unit import Unit


class Cell:
    def __init__(self, obj=None):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj


class Field:
    def __init__(self, field: list[Cell], unit: Unit, cols: int, rows: int):
        self.field = field
        self.unit = unit
        self.cols = cols
        self.rows = rows

    def get_cell(self, x, y):
        return self.field[y][x]

    def move_unit_up(self):
        x, y = self.unit.get_coordinates()
        y -= 1
        if self.get_cell(x, y).get_object().get_terrain() != 'Wall' and (y >= 0):
            self.get_cell(x, y).get_object().step_on(self.unit)
            self.unit.set_coordinates(x, y)
        # print("hp:", self.unit.get_hp())
        # print("key:", self.unit.has_key_())
        # print("is_alive:", self.unit.is_alive())

    def move_unit_down(self):
        x, y = self.unit.get_coordinates()
        y += 1
        if self.get_cell(x, y).get_object().get_terrain() != 'Wall' and (y < self.rows):
            self.get_cell(x, y).get_object().step_on(self.unit)
            self.unit.set_coordinates(x, y)
        # print("hp:", self.unit.get_hp())
        # print("key:", self.unit.has_key_())
        # print("is_alive:", self.unit.is_alive())

    def move_unit_right(self):
        x, y = self.unit.get_coordinates()
        x += 1
        if self.get_cell(x, y).get_object().get_terrain() != 'Wall' and (x < self.cols):
            self.get_cell(x, y).get_object().step_on(self.unit)
            self.unit.set_coordinates(x, y)
        # print("hp:", self.unit.get_hp())
        # print("key:", self.unit.has_key_())
        # print("is_alive:", self.unit.is_alive())

    def move_unit_left(self):
        x, y = self.unit.get_coordinates()
        x -= 1
        if self.get_cell(x, y).get_object().get_terrain() != 'Wall' and (x >= 0):
            self.get_cell(x, y).get_object().step_on(self.unit)
            self.unit.set_coordinates(x, y)
        # print("hp:", self.unit.get_hp())
        # print("key:", self.unit.has_key_())
        # print("is_alive:", self.unit.is_alive())

    def get_field(self):
        return self.field

    def get_cols(self):
        return self.cols

    def get_rows(self):
        return self.rows

    def cell(self):
        return self.unit
