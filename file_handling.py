from class_definition import *


def get_board(is_start, question):
    boards = question["board"]
    if is_start:
        board = Matrix(boards["start"])
    else:
        board = Matrix(boards["goal"])

    return board


def get_all_dies(question):
    dies: list[Die]
    dies = []
    general = question["general"]
    n = general["n"]
    patterns = general["patterns"]
    for pattern in patterns :
        die = Die(index=pattern["p"], matrix=pattern["cells"])
        dies.append(die)

    return dies
