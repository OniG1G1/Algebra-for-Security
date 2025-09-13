from modular_arithmetic.addition import Addition
from modular_arithmetic.subtraction import Subtraction
from modular_arithmetic.reduction import Reduction

class ModularArithmetic:
    def __init__(self):
        # Router: maps operation name → operation class
        self.operations = {
            "addition": Addition().execute,
            "subtraction": Subtraction().execute,
            "reduction": Reduction().execute 
        }

    def findOperation(self, exercise: dict):
        op_name = exercise.get("operation")
        if op_name in self.operations:
            return self.operations[op_name](exercise)
        else:
            raise ValueError(f"Unknown operation: {op_name}")
