import api_handling as api
import file_handling
import file_handling as file
import solve as solve

# Set question
question_id = 11

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
print(solve.compare(start_board, goal_board))

# Get all dies
dies = file_handling.get_all_dies(question)
for die in dies :
    die.display()

# Solving


# Ouput Handling
