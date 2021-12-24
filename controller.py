from unit import Ghost
from terrain import Wall, Grass, Key, Trap, Door
from field import Cell, Field
from constants import HIT_POINTS


class GameController:
    # длинный список параметров
    # предлагаю убрать hero: Ghost = None(см. ниже), hp=HIT_POINTS(т.к. мы импортируем его из констант)
    def __init__(self, maze: str, hero: Ghost = None, hp=HIT_POINTS):
        self.mapping = {
            "Wall": "🔲",
            "Grass": "🍀",  # '⬜️',
            "Ghost": "👻",
            "Key": "🗝",
            "Door": "🚪",
            "Trap": "💀",
        }
        self.game_on = True
        self.hero = hero
        self.field = None
        self.make_field(maze, hp=hp)

    @staticmethod
    def _make_field_template(template: str) -> list:
        return [[i for i in line.strip()] for line in template.strip().split("\n")]

    # Запах "Длинный метод". В данной функции мы:
        # 1. создаем массив массивов из объектов Cell
        # 2. переопределяем параметр класса GameController.field
        # 3. (возможно неуместно и выходит за рамки домашнего задания)
        # Переопределяем свой параметр if not self.hero:
        #                                  self.hero = Ghost([item_n, line_n], hp=hp)
    # Предлагаю:
        # 1. Оставляем как есть.
        # 2. class GameController:
        #     def __init__(self, maze: str, hp=HIT_POINTS):
        #         self.hero = Ghost([-1, -1], hp=hp)
        #         self.field = Field(field=make_field(maze), unit=self.hero, cols=len(fields[0]), rows=len(fields))
        #     При этом make_field должно возвращать field с ячейками Cell с объектами и проверять, передались ли
        #     координаты в self.hero(был ли вообще герой на карте).
        #     if self.hero.coord == [-1,-1]:
        #         raise WrongMaze as e:
        #           print(e)
        # 3. В функции make_field, думаю, достаточно переопределить свойство своего объекта, а не весь класс:
        #         def make_field(self, level_string: str):
        #                     if item == 'G':
        #                         field_line.append(Cell(Grass()))
        #                         self.hero.coord = Ghost([item_n, line_n])
    # Не знаю какой запах.
    #   наименования item_n, line_n без кода не поймешь.
    # Предлагаю:
    #   Переименовать переменные в x_coord, y_coord, так как они, по сути, в нашем контексте,
    #   определяют положение объекта на карте
    def make_field(self, level_string: str, hp: int):
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
                    if not self.hero:
                        self.hero = Ghost([item_n, line_n], hp=hp)
                if item == "K":
                    field_line.append(Cell(Key()))
                if item == "D":
                    field_line.append(Cell(Door()))
                if item == "T":
                    field_line.append(Cell(Trap()))
            fields.append(field_line)

        self.field = Field(field=fields, unit=self.hero)

    # длинный метод
    # т.к. Play отвечает за общую игровую логику, предлагаю выбор направления перемещения вынести в отдельную функцию
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
        for y, line in enumerate(self.field.get_field()):
            s = ""
            for x, item in enumerate(line):
                if self.hero.has_position(x, y):
                    s += self.mapping["Ghost"]
                else:
                    s += self.mapping[item.get_object().get_terrain()]
            print(s)
