import api_handling as api
from class_definition import Matrix
from class_definition import Operation
import file_handling as file

# Set question
question_id = 11

question = api.get_question(question_id)

# Get Start Board
print("Start Board---------------------------------------")
start_board = file.get_board(is_start=True, question=question)
start_board.display()

# Get Goal Board
print("Goal Board----------------------------------------")
goal_board = file.get_board(is_start=False, question=question)
goal_board.display()
