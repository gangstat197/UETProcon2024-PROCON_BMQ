from die import *

def compare(a, b):
    difference_count = 0

    # Compare the matrices element-wise and count differences
    for i in range(a.m):
        for j in range(a.n):
            if a.matrix[i][j] != b.matrix[i][j]:
                difference_count += 1

    def __init__(self, x: int, y: int, dir: str, matrix: list[list[int]]):
        self.dir = dir
        self.x = x
        self.y = y
        self.matrix = matrix

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

    def display(self):
        for row in self.matrix:
            print(row)
