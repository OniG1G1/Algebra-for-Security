class Arithmetic:
    """
    Base class for arithmetic types (e.g., IntegerArithmetic, ModularArithmetic).
    Provides a common interface for registering and dispatching operations.
    """

    operations: dict[str, callable] = {}  # subclasses override

    def findOperation(self, exercise: dict):
        """
        Dispatch to the appropriate operation based on exercise['operation'].
        """
        op_name = exercise.get("operation")
        if op_name not in self.operations:
            raise ValueError(f"Unknown operation: {op_name}")
        return self.operations[op_name](exercise)
