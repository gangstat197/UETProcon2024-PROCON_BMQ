from class_definition import *
import copy
#We will solve this problem using only fixed dies
def solve(init: Matrix, final: Matrix) -> list[Operation]:
     init = init.matrix
     final = final.matrix
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
                              o.display()
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

