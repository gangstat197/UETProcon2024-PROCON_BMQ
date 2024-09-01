from class_definition import *
import random

def generate_pair(m: int, n: int):
    lst = []
    for i in range(m):
        for j in range(n):
            lst.append((i, j))
    return lst
def get_direction_index(k : int):
    a = dir_lst[k//16 % 4]
    b = dir_lst[k//4 % 4]
    c = dir_lst[k % 4]
    return [a, b, c]
def solve_3moves(start: Matrix, goal: Matrix, dies: list[Die]) -> list[Operation]:
    lst = generate_pair(start.m, start.n)
    best_operations : list[Operation]
    best_diff = compare(start, goal)
    for pair_1 in lst:
        for pair_2 in lst:
            for pair_3 in lst:
                for k in range(0, 64):
                    dirs = get_direction_index(k)
                    for die_index, die in enumerate(dies):
                        o1 = Operation(die_index, *pair_1, dirs[0], die)
                        o2 = Operation(die_index, *pair_2, dirs[1], die)
                        o3 = Operation(die_index, *pair_3, dirs[2], die)
                        copy_matrix = clone(start)
                        copy_matrix.die_cutting(o1)
                        copy_matrix.die_cutting(o2)
                        copy_matrix.die_cutting(o3)
                        cur_diff = compare(copy_matrix, goal)
                        if (cur_diff < best_diff):
                            best_diff = cur_diff
                            best_operations = [o1, o2, o3]
                            if (cur_diff == 0):
                                print("Found 100% accurate solution!")
                                return best_operations

    return best_operations

