labirinth = """
WWWWWWWWWW
WggGgggggW
WgTTTggDgW
WKggggTggW
WWWWWWWWWW
"""

labt = """
1 0 0 0 1 0 
0 0 1 1 0 0 
0 1 1 1 1 1
"""


def make_field(template):
    return [line.strip().split(" ") for line in template.strip().split("\n")]


def make_field_1(template):
    return [[i for i in line.strip()] for line in template.strip().split("\n")]


print(*make_field(labt), sep="\n")
print(*make_field_1(labirinth), sep="\n")
