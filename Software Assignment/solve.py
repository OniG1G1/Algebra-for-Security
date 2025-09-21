import json
from exercise import compute_exercise, print_exercise

def solve_exercise(exercise_location: str, answer_location: str):
    exercise = extract_exercise(exercise_location)
    
    answer = compute_exercise(exercise)

    load_answer(answer_location, answer)
    
    print("Exercise solved!")
    
    print_exercise(answer)
        
### --- Helper Methods --- ###
    
def extract_exercise(exercise_location: str) -> dict:
    
    print(f"Extracting exercise from: {exercise_location}...")
    
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)
        return exercise
    
def load_answer(answer_location: str, answer: dict) -> None:
    
    print(f"Loading answer into: {answer_location}...")
    
    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)


### --- Main --- ###

if __name__ == "__main__":
    solve_exercise("exercises/exercise.json", "answers/answer.json")