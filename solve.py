from class_definition import *

#We will solve this problem using only fixed dies
def solve(init: Matrix, final: Matrix) -> list[Operation]:
     pass

def compare(a, b):
     difference_count = 0

     # Compare the matrices element-wise and count differences
     for i in range(a.m):
          for j in range(a.n):
               if a.matrix[i][j] != b.matrix[i][j]:
                    difference_count += 1
     return difference_count

# Example
B = [[1, 2, 3], 
     [4, 0, 6], 
     [7, 8, 9]]
G = [[1,2,3],
     [4,5,6],
     [7,8,9]]

P = [[1, 0],  #die
     [1, 1]]

ma = Matrix(B)
op = Operation(1, 1, 'right', P)
ma.die_cutting(op)
ma.display()
