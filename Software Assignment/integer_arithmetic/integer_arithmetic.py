#from arithmetic.core import Arithmetic
from integer_arithmetic.addition import Addition
from integer_arithmetic.subtraction import Subtraction
from integer_arithmetic.multiplication import Multiplication
from integer_arithmetic.karatsuba import Karatsuba
from integer_arithmetic.extended_euclidean import ExtendedEuclidean


class IntegerArithmetic():
    def __init__(self):
        # Router: maps operation name → operation class
        self.operations = {
            "addition": Addition().execute,
            "subtraction": Subtraction().execute,
            "multiplication": Multiplication().execute,
            "multiplication_primary": Multiplication().execute,
            "multiplication_karatsuba": Karatsuba().execute,
            "extended_euclidean_algorithm": ExtendedEuclidean().execute

        }

    def findOperation(self, exercise: dict):
        op_name = exercise.get("operation")
        if op_name in self.operations:
            return self.operations[op_name](exercise)
        else:
            raise ValueError(f"Unknown operation: {op_name}")
