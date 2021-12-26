from unit import Ghost
from terrain import Wall, Grass, Key, Trap, Door
from field import Cell, Field
from constants import HIT_POINTS
from errors import NoHeroError
import os


class GameController:
    def __init__(self, maze: str):
        self.mapping = {
            "Wall": "🔲",
            "Grass": "🍀",  # '⬜️',
            "Ghost": "👻",
            "Key": "🗝",
            "Door": "🚪",
            "Trap": "💀",
        }
        self.game_on = True
        self.hero = None
        self.field = None
        self.make_field(maze)

    @staticmethod
    def _make_field_template(template: str) -> list:
        return [[i for i in line.strip()] for line in template.strip().split("\n")]

    def make_field(self, level_string: str):
        field_template = self._make_field_template(level_string)
        fields = []
        for line_n, line in enumerate(field_template):
            field_line = []
            for item_n, item in enumerate(line):
                if item == "W":
                    field_line.append(Cell(Wall()))
                if item == "g":
                    field_line.append(Cell(Grass()))
                if item == "G":
                    field_line.append(Cell(Grass()))
                    self.hero = Ghost([item_n, line_n], hp=HIT_POINTS)
                if item == "K":
                    field_line.append(Cell(Key()))
                if item == "D":
                    field_line.append(Cell(Door()))
                if item == "T":
                    field_line.append(Cell(Trap()))
            fields.append(field_line)

        if self.hero is None:
            raise NoHeroError

        self.field = Field(field=fields, unit=self.hero)

    def play(self):
        self._draw_field()
        while self.game_on and not self.hero.escaped:
            command = input()
            if command == "a":
                self.field.move_unit_left()
            if command == "w":
                self.field.move_unit_up()
            if command == "d":
                self.field.move_unit_right()
            if command == "s":
                self.field.move_unit_down()
            if command in ["stop", "exit"]:
                self.game_on = False

            self._draw_field()

        if self.hero.escaped:
            print("Поздравляю! Вы нашли выход!")

        if not self.game_on:
            print("Нам жаль, что Вы уходите. Приходите еще!")

    def _draw_field(self):
        # os.system('cls||clear')
        for y, line in enumerate(self.field.get_field()):
            s = ""
            for x, item in enumerate(line):
                if self.hero.has_position(x, y):
                    s += self.mapping["Ghost"]
                else:
                    s += self.mapping[item.get_object().get_terrain()]
            print(s)
