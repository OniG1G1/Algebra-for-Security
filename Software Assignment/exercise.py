import json

from integer_arithmetic.base import IntegerArithmetic
from modular_arithmetic.base import ModularArithmetic

def compute_exercise(exercise: dict) -> dict:
    
    print("Computing exercise...")
    
    arithmetic_type = findType(exercise["type"])
    operation = arithmetic_type.findOperation(exercise["operation"])
    
    answer = operation(exercise)
    return answer

def print_exercise(exercise: dict) -> None:
    print(json.dumps(exercise, indent=4, sort_keys=True))

def findType(type_name: str):
    
    print("Finding arithmetic type of exercise...")
    
    if type_name == "integer_arithmetic":
        arithmetic_type = IntegerArithmetic()
    elif type_name == "modular_arithmetic":
        arithmetic_type = ModularArithmetic()
    else:
        raise ValueError(f"Unknown exercise type: {type_name}")
    
    print(f"Using type: {type(arithmetic_type).__name__}")
    return arithmetic_type
