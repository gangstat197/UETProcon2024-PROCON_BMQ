from solve import *
from solve_3moves import *

# Example
B = [[1, 2, 3],
     [4, 0, 6],
     [7, 8, 9]]
G = [[1, 2, 3],
     [4, 6, 0],
     [7, 9, 8]]

P = [[1, 0],  # die
     [1, 0]]

ma = Matrix(B)
op = Operation(1, 0, 0, 'left', P)
ma.die_cutting(op)
op = Operation(1, 1, 1, 'right', P)
ma.die_cutting(op)
op = Operation(0, 0, 1, 'up', P)
ma.die_cutting(op)
ma.display()
B = [[1, 2, 3],
     [4, 0, 6],
     [7, 8, 9]]
# G = [[1, 2, 3],
#      [4, 6, 0],
#      [7, 9, 8]]
fixed_dies = generate_fixed_die()
solve(Matrix(B), ma, fixed_dies, 10)
# solve_3moves(Matrix(B), ma, fixed_dies)
