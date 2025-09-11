# Import built-in json library for handling input/output
import json

from integerArithmetic import IntegerArithmetic
from modularArithmetic import ModularArithmetic

def solve_exercise(exercise_location: str, answer_location: str):
    with open(exercise_location, "r") as exercise_file:
        # Deserialize JSON exercise data
        exercise = json.load(exercise_file)

        # Dispatch based on type
        exercise_type = findType(exercise["type"])

        print(f"Using type: {type(exercise_type).__name__}")
        
        # Dispatch based on operation
        answer = exercise_type.findOperation(exercise)
        #result = findType(exercise["type"]).findOperation(exercise)
        
        # Open file at answer_location for writing, creating the file if it does not exist yet (and overwriting it if it does already exist).
    with open(answer_location, "w") as answer_file:
        # Serialize Python answer data (stored in answer) to JSON answer data and write it to answer_file
        json.dump(answer, answer_file, indent=4)



def findType(type_name: str):
    if type_name == "integer_arithmetic":
        return IntegerArithmetic()
    elif type_name == "modular_arithmetic":
        return ModularArithmetic()
    else:
        raise ValueError(f"Unknown exercise type: {type_name}")


# -- MAIN -- #
if __name__ == "__main__":
    solve_exercise("question.json", "answer.json")
