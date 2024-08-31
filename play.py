import api_handling as api
import file_handling
import file_handling as file
from class_definition import *
from solve import *

# Set question
question_id = 34

question = api.get_question(question_id)

# Input Handling

# Get Start Board
print("Start Board---------------------------------------")
start_board = file.get_board(is_start=True, question=question)
start_board.display()

# Get Goal Board
print("Goal Board----------------------------------------")
goal_board = file.get_board(is_start=False, question=question)
goal_board.display()

# The number of different cells
print("Initial Differences: ", compare(start_board, goal_board))

# Get fixed dies from code
fixed_dies = generate_fixed_die()
# Get general dies from server
general_dies = file_handling.get_all_dies(question)

# Sum up all dies
dies = fixed_dies + general_dies
for die in dies:
    if die.index < 10 or die.index > 24:
        die.display()

# Answers settings----------------
# Dies: list of Die
# Moves: maximum moves
# Return: A list of Operations

moves = 1

# Hard-core Solve here
operations = solve(start_board, goal_board, dies, moves)

# Output
ans_name: str
ans_name = f"question_{question_id}_solution"

file.create_answer_file(operations, ans_name)

# Random Solve here
test_size = 1000000
rand_operations = random_solve(start_board, goal_board, dies, moves, test_size)

# Random Output
rand_ans_name: str
rand_ans_name = f"question_{question_id}_random_solution"

file.create_answer_file(rand_operations, rand_ans_name)

# Testing

# test_operations = [Operation(1, 1, 1, "bottom", [[1, 1]]),
#                    Operation(1, 2, 2, "top", [[1, 1]]),
#                    ]
# # Testing Only
# file.create_answer_file(test_operations, ans_name)
