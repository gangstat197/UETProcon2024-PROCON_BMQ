from solve import *

# Example
B = [[1, 2, 3], 
     [4, 0, 6], 
     [7, 8, 9]] 
G = [[1, 2, 3],
     [4, 6, 0],
     [7, 9, 8]]

P = [[1, 0],  #die
     [1, 0]]

ma = Matrix(B)
op = Operation(0, 0, 'left', P)
ma.die_cutting(op)
ma.display()
B = ((1, 2, 3),
     (4, 0, 6),
     (7, 8, 9))
G = ((1, 2, 3),
     (4, 6, 0),
     (7, 9, 8))
solve(Matrix(B), Matrix(G))
B = ((1, 2, 3),
     (4, 0, 6),
     (7, 8, 9))
G = ((2, 3, 1),
     (0, 6, 4),
     (8, 9, 7))
solve(Matrix(B), Matrix(G))