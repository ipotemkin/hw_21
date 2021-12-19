from controller import GameController

maze = """
WWWWWWWWWW
WggGgggggW
WgTTTggDgW
WKggggTggW
WWWWWWWWWW
"""


if __name__ == "__main__":
    gc = GameController(maze)
    gc.play()
