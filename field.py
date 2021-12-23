from unit import Unit


class Cell:
    def __init__(self, obj=None):
        self.obj = obj

    def get_object(self):
        return self.obj

    def set_object(self, obj):
        self.obj = obj


class Field:
    def __init__(self, field: list[list[Cell]], unit: Unit):
        self.field = field
        self.unit = unit

    def get_cell(self, x, y):
        return self.field[y][x]

    def _do_move(self, x, y):
        step_on_object = self.get_cell(x, y).get_object()
        step_on_object.step_on(self.unit)
        if step_on_object.is_walkable():
            self.unit.set_coordinates(x, y)

    def move_unit_up(self):
        x, y = self.unit.get_coordinates()
        self._do_move(x, y - 1)

    def move_unit_down(self):
        x, y = self.unit.get_coordinates()
        self._do_move(x, y + 1)

    def move_unit_right(self):
        x, y = self.unit.get_coordinates()
        self._do_move(x + 1, y)

    def move_unit_left(self):
        x, y = self.unit.get_coordinates()
        self._do_move(x - 1, y)

    def get_field(self):
        return self.field

    def cell(self):
        return self.unit
