# Import built-in json library for handling input/output
import json

from integer_arithmetic.integer_arithmetic import IntegerArithmetic
from modular_arithmetic.modular_arithmetic import ModularArithmetic


def solve_exercise(exercise_location: str, answer_location: str):
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    exercise_type = findType(exercise["type"])
    print(f"Using type: {type(exercise_type).__name__}")

    answer = exercise_type.findOperation(exercise)
    print("DEBUG: answer returned:", answer)

    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)
        
### --- Helper Methods --- ###
        
# TODO: Implement Modular Arithmetic
def findType(type_name: str):
    if type_name == "integer_arithmetic":
        return IntegerArithmetic()
    elif type_name == "modular_arithmetic":
        return ModularArithmetic()
    else:
        raise ValueError(f"Unknown exercise type: {type_name}")

### --- Main --- ###
if __name__ == "__main__":
    solve_exercise("exercises/exercise.json", "answers/answer.json")