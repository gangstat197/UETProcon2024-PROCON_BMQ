import random

from class_definition import *


# We will solve this problem using only fixed dies


def solve(start: Matrix, goal: Matrix, dies: list[Die], max_move: int) -> list[Operation]:
    operations: list[Operation]
    operations = []
    directions = ["top", "bottom", "left", "right"]

    best_score = goal.m * goal.n
    current_best_matrix = start

    current_moves = max_move

    while current_moves > 0:
        print("Move Number: {}".format(current_moves))
        current_moves -= 1
        current_matrix = current_best_matrix
        best_operation: Operation

        for die_index, die in enumerate(dies):
            if die_index < 25 and min(die.m, die.n) > max(current_best_matrix.m, current_best_matrix.n):
                continue

            for i in range(len(current_best_matrix.matrix)):
                for j in range(len(current_best_matrix.matrix[0])):
                    for direction in directions:
                        operation = Operation(index=die_index, x=i, y=j, direction=direction, matrix=die.matrix)

                        copy_matrix = current_best_matrix
                        copy_matrix.die_cutting(operation)

                        diff = compare(copy_matrix, goal)
                        if diff <= best_score:
                            best_operation = operation
                            best_score = diff
                            current_matrix = copy_matrix
                            print("Current Best Score: {}".format(best_score))

        operations.append(best_operation)
        current_best_matrix = current_matrix

    return operations


def random_solve(start: Matrix, goal: Matrix, dies: list[Die], max_move: int, test_size: int):
    operations: list[Operation]
    operations = []
    directions = ["top", "bottom", "left", "right"]

    best_score = goal.m * goal.n

    while test_size > 0:
        test_size -= 1
        curr_operations = []
        clone_matrix = start
        while max_move > 0:
            max_move -= 1

            random_direction = random.choice(directions)
            random_x = random.randint(0, len(start.matrix))
            random_y = random.randint(0, len(start.matrix[0]))
            random_index = random.randint(0, len(dies) - 1)
            random_die = dies[random_index]

            random_operation = Operation(index=random_index, matrix=random_die.matrix,
                                         x=random_x, y=random_y,
                                         direction=random_direction)
            curr_operations.append(random_operation)

        for operation in curr_operations:
            clone_matrix.die_cutting(operation)

        diff = compare(clone_matrix, goal)
        if diff <= best_score:
            operations = curr_operations
            best_score = diff
            print("Current Best Score: {}".format(best_score))

    return operations


def compare(a, b):
    difference_count = 0

    # Compare the matrices element-wise and count differences
    for i in range(a.m):
        for j in range(a.n):
            if a.matrix[i][j] != b.matrix[i][j]:
                difference_count += 1
    return difference_count
