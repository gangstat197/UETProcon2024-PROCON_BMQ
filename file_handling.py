import json
import os

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
    for pattern in patterns:
        die = Die(index=pattern["p"], matrix=pattern["cells"])
        dies.append(die)

    return dies


def create_answer_file(operations: list[Operation], file_name: str):
    n = len(operations)
    operation_data = [operation.to_json() for operation in operations]

    json_data = {
        "n": n,
        "ops": operation_data
    }

    solutions_path = "Solutions"
    if not os.path.exists(solutions_path):
        os.makedirs(solutions_path)

    file_path = os.path.join(solutions_path, file_name)
    with open(file_path, "w") as f:
        json.dump(json_data, f, indent=2)
