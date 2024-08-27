class Operation:
    # direction can be [left, right, up, down]
    dir: str
    x: int
    y: int
    matrix: list[list[int]]

    def __init__(self, x: int, y: int, dir: str, matrix: list[list[int]]):
        self.dir = dir
        self.x = x
        self.y = y
        self.matrix = matrix
