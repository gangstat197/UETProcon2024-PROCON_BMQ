from class_definition import *
import copy
#We will solve this problem using only fixed dies
def solve(init: Matrix, final: Matrix) -> list[Operation]:
     final_obj = Matrix([list(i) for i in final])
     for die in die_lst:
          # print("die:", die)
          for i in range(len(init)):
               for j in range(len(init[0])):
                    for dir in dir_lst:
                         copyc = Matrix([list(i) for i in init])
                         o = Operation(i, j, dir, die)
                         # print(o.matrix)
                         copyc.die_cutting(o)
                         # copyc.display()
                         if (copyc.compare(final_obj)):
                              print("Found matrix")
                              print(o.matrix)
                              return [o]
     print("Warning!! Cannot find suitable move")
     return []
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
     [4, 0, 6], # 0 4 6
     [7, 8, 9]] # 8 7 9
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
solve(B, G)