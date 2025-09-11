class IntegerArithmetic:
    def __init__(self):
        self.operations = {
            "addition": self.addition
        }

    def addition(self, exercise):
        x = exercise["x"]
        y = exercise["y"]
        result = x + y
        
        print(f"Result of addition: {result}")
        print("Also this works.")
        return {"answer": result}

    def findOperation(self, exercise):
        op_name = exercise.get("operation")
        if op_name in self.operations:
            print("Executing operation:", op_name)
            return self.operations[op_name](exercise)
        else:
            raise ValueError(f"Unknown operation: {op_name}")
