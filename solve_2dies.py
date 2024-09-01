from class_definition import *

# def solve(init : Matrix, final: Matrix, die_lst: list[Die]) -> list[Operation]:
#     for die_1 in die_lst:
#         for die_2 in die_lst:
#             for i in range(init.m):
#                 for j in range(init.n):
#                     if (init.matrix[i][j] == final.matrix[i][j]):
#                         continue

#                     for dir in dir_lst:
#                         o = Operation(i, j, dir, die_1)
#                         o2 = Operation()
#     print("Warning!! Cannot find suitable solution")
def solve(init: Matrix, final: Matrix, die_lst : list[Die]) -> list[Operation]:
    directions = ['left', 'right', 'up', 'down']
    operations = []

    # Attempt to reverse the operation
    def is_equal(m1: Matrix, m2: Matrix) -> bool:
        return m1.matrix == m2.matrix

    for pattern in die_lst:
            for direction in directions:
                for y in range(init.m ):
                    for x in range(init.n ):
                        op = Operation(x, y, direction, pattern)
                        temp_final = Matrix([row[:] for row in final.matrix])
                        temp_final.die_cutting(op)
                        if is_equal(temp_final, init):
                            operations.append(op)
                            final.die_cutting(op)  # Apply reverse operation to final
                            if is_equal(init, final):
                                return operations
    return operations