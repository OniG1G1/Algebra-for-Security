from arithmetic.base import Arithmetic
from integer_arithmetic.addition import Addition
from integer_arithmetic.subtraction import Subtraction

class IntegerArithmetic(Arithmetic):
    def __init__(self):
        # Router: maps operation name → operation class
        self.operations = {
            "addition": Addition().execute,
            "subtraction": Subtraction().execute
        }

    def findOperation(self, exercise: dict):
        op_name = exercise.get("operation")
        if op_name in self.operations:
            return self.operations[op_name](exercise)
        else:
            raise ValueError(f"Unknown operation: {op_name}")
