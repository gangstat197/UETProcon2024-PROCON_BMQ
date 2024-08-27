from Problem.board import *
from die import *

#We will solve this problem using only fixed dies
def solve(init: Matrix, final: Matrix) -> list[Operation]:
    pass

# Example
B = [[1, 2, 3], 
     [4, 0, 6], 
     [7, 8, 9]]
G = [[1,2,3],
     [4,5,6],
     [7,8,9]]

P = [[1, 0], 
     [1, 1]]

ma = Matrix(B)
op = Operation(1, 1, 'right', P)
ma.die_cutting(op)
ma.display()
