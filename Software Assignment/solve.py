# Import built-in json library for handling input/output
import json

from integer_arithmetic.integer_arithmetic import IntegerArithmetic

def solve_exercise(exercise_location: str, answer_location: str):
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    exercise_type = findType(exercise["type"])
    print(f"Using type: {type(exercise_type).__name__}")

    answer = exercise_type.findOperation(exercise)

    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)
        
### --- Helper Methods --- ###
        
# TODO: Implement Modular Arithmetic
def findType(type_name: str):
    if type_name == "integer_arithmetic":
        return IntegerArithmetic()
    elif type_name == "modular_arithmetic":
        raise NotImplementedError("Modular arithmetic not implemented yet")
    else:
        raise ValueError(f"Unknown exercise type: {type_name}")

### --- Main --- ###
if __name__ == "__main__":
    solve_exercise("exercises/exercise.json", "answers/answer.json")