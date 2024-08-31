import copy


class Die:
    matrix: list[list[int]]

    # index
    index: int
    # columns
    col: int
    # rows
    row: int

    def __init__(self, index, matrix: list[list[int]]):
        self.matrix = matrix
        self.index = index
        self.n = len(matrix[0])
        self.m = len(matrix)

    def display(self):
        print("Die number: ", self.index)
        for row in self.matrix:
            print(row)


class Operation:
    # die number
    index: int

    # die applied positions
    x: int
    y: int

    # direction can be [left, right, up, down]
    dir: str

    # operation matrix
    matrix: list[list[int]]

    def __init__(self, index: int, x: int, y: int, direction: str, matrix: list[list[int]]):
        self.index = index

        self.x = x
        self.y = y

        self.dir = direction
        self.matrix = matrix

    def get_direction(self):
        match_dir = {
            "top": 0,
            "bottom": 1,
            "left": 2,
            "right": 3,
        }

        return match_dir.get(self.dir)

    def to_json(self):
        return {
            "p": self.index,
            "x": self.x,
            "y": self.y,
            "s": self.get_direction()
        }

    def display(self):
        print("index: {}, x : {}, y: {}, direction: {}".format(self.dir, self.x, self.y, self.dir))
        for row in self.matrix:
            print(row)


class Matrix:
    matrix: list[list[int]]
    # columns
    n: int
    # rows
    m: int

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.n = len(matrix[0])
        self.m = len(matrix)

    def die_cutting(self, o: Operation):
        p, q = len(o.matrix), len(o.matrix[0])  # Dimensions of the pattern

        # Step 1: Determine the positions to "lift" based on the pattern
        lifted_positions = []
        for i in range(p):
            for j in range(q):
                if o.matrix[i][j] == 1:  # Only lift if the pattern value is 1
                    bx, by = o.x + j, o.y + i
                    if 0 <= bx < self.n and 0 <= by < self.m:
                        lifted_positions.append((by, bx))

        # Step 2: Lift elements by setting them to None
        lifted_elements = [self.matrix[by][bx] for by, bx in lifted_positions]
        for by, bx in lifted_positions:
            self.matrix[by][bx] = None

        # Step 3: Shift remaining elements according to the direction
        if o.dir == 'up':
            for bx in range(self.n):
                col = [self.matrix[by][bx] for by in range(self.m) if self.matrix[by][bx] is not None]
                for by in range(self.m):
                    self.matrix[by][bx] = col.pop(0) if col else None
        elif o.dir == 'down':
            for bx in range(self.n):
                col = [self.matrix[by][bx] for by in range(self.m) if self.matrix[by][bx] is not None]
                for by in range(self.m - 1, -1, -1):
                    self.matrix[by][bx] = col.pop() if col else None

        elif o.dir == 'left':
            for by in range(self.m):
                row = [self.matrix[by][bx] for bx in range(self.n) if self.matrix[by][bx] is not None]
                for bx in range(self.n):
                    self.matrix[by][bx] = row.pop(0) if row else None
        elif o.dir == 'right':
            for by in range(self.m):
                row = [self.matrix[by][bx] for bx in range(self.n) if self.matrix[by][bx] is not None]
                for bx in range(self.n - 1, -1, -1):
                    self.matrix[by][bx] = row.pop() if row else None

        # Step 4: Place the lifted elements back into the matrix
        empty_positions = [(by, bx) for by in range(self.m) for bx in range(self.n) if self.matrix[by][bx] is None]
        for pos, elem in zip(empty_positions, lifted_elements):
            self.matrix[pos[0]][pos[1]] = elem

    # def die_cutted(self, o : Operation):

    def display(self):
        for row in self.matrix:
            print(row)

    def compare(self, other) -> bool:
        if other.m != self.m and other.n != self.n:
            print("Warning! Two matrix aren't a same size")
            return False
        return self.matrix == other.matrix


def clone(ma: Matrix):
    return Matrix(copy.deepcopy(ma.matrix))


def generate_fixed_die() -> list[Die]:
    size_lst = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    die_lst: list[Die]
    die_lst = [Die(0, [[1]])]

    cur_index = 0
    for size in size_lst:
        if size == 1:
            continue

        # Generate the matrex of 3 types of Die
        die_type1 = [[1] * size for i in range(size)]
        die_type2 = [[0] * size for i in range(size)]
        die_type3 = [[0] * size for i in range(size)]

        for i in range(size):
            for j in range(size):
                if i % 2 == 0:
                    die_type2[i][j] = 1

        for i in range(size):
            for j in range(size):
                if j % 2 == 0:
                    die_type3[i][j] = 1

        die_lst.extend([Die(cur_index + 1, die_type1), Die(cur_index + 2, die_type2), Die(cur_index + 3, die_type3)])
        cur_index += 3

    return die_lst
