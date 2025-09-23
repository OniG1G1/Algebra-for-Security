from modular.core import modularReduction

class Reduction:
    def execute(self, exercise: dict) -> dict:
        """
        Main entry point for reduction.
        """
        print(f"Executing operation: {type(self).__name__}")
        x = exercise["x"]
        y = exercise["y"]
        radix = int(exercise["radix"])
        m = exercise["modulus"]
        result = modularReduction(x, y, radix, m)
        return {"answer": result}
