import json

import time

from exercise import compute_exercise, print_exercise

def solve_exercise(exercise_location: str, answer_location: str):
    
    start_time = time.time()  # start timing
    
    exercise = extract_exercise(exercise_location)
    
    answer = compute_exercise(exercise)

    load_answer(answer_location, answer)
    
    end_time = time.time()  # end timing
    duration = end_time - start_time
    
    print("Exercise solved! \n")
    
    print_exercise(answer)
    
    print(f"Time taken: {duration:.4f} seconds")
    

        
### --- Helper Methods --- ###
    
def extract_exercise(exercise_location: str) -> dict:
    
    print(f"\nExtracting exercise from: {exercise_location}...")
    
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