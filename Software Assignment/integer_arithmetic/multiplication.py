from arithmetic.core import multiply

class Multiplication:
    def execute(self, exercise: dict) -> dict:
        """
        Main entry point for Multiplication. Handles sign routing.
        """
        print(f"Executing operation: {type(self).__name__}")
        x = exercise["x"]
        y = exercise["y"]
        radix = int(exercise["radix"])
        result = self.run(x, y, radix)
        return {"answer": result}
    
    def run(self, x: str, y: str, radix: int) -> str:
        sign_x = '-' if x.startswith('-') else '+'
        sign_y = '-' if y.startswith('-') else '+'

        # Remove signs for raw digit handling
        x_val = x[1:] if sign_x == '-' else x
        y_val = y[1:] if sign_y == '-' else y

        router = {
            ('+', '+'): self._pos_pos,
            ('-', '-'): self._neg_neg,
            ('+', '-'): self._pos_neg,
            ('-', '+'): self._neg_pos,
        }

        handler = router[(sign_x, sign_y)]
        return handler(x_val, y_val, radix)
    
    # -----------------------------
    # Cases
    # -----------------------------

    def _pos_pos(self, x: str, y: str, radix: int) -> str:
        """
        Case: positive + positive.
        (+x) * (+y) = x * y
        """
        return multiply(x, y, radix, negative=False)

    def _neg_neg(self, x: str, y: str, radix: int) -> str:
        """
        Case: negative + negative.
        (-x) * (-y) = x * y
        Equivalent to pos_pos
        """
        return multiply(x, y, radix, negative=False)

    def _pos_neg(self, x: str, y: str, radix: int) -> str:
        """
        Case: positive + negative.
        (+x) * (-y) = -(x * y)
        """
        return multiply(x, y, radix, negative=True)
    
    def _neg_pos(self, x: str, y: str, radix: int) -> str:
        """
        Case: negative + postive.
        (-x) * (+y) = -(x * y)
        Equivalent to pos_neg
        """
        return multiply(x, y, radix, negative=True)
    
    """def execute(self, exercise: dict) -> dict:
        
        Main entry point for multiplication. Handles sign routing.
        
        print(f"Executing operation: {type(self).__name__}")
        x = exercise["x"]
        y = exercise["y"]
        radix = int(exercise["radix"])

        sign_x = '-' if x.startswith('-') else '+'
        sign_y = '-' if y.startswith('-') else '+'

        # Remove signs for raw digit handling
        x_val = x[1:] if sign_x == '-' else x
        y_val = y[1:] if sign_y == '-' else y

        router = {
            ('+', '+'): self._pos_pos,
            ('-', '-'): self._neg_neg,
            ('+', '-'): self._pos_neg,
            ('-', '+'): self._neg_pos,
        }

        handler = router[(sign_x, sign_y)]
        result = handler(x_val, y_val, radix)

        return {"answer": result}"""
    
def multiplication(exercise: dict) -> dict:
    """
    Main entry point for multiplication. Handles sign routing.
    """

    print("Executing 'multiplication' operation...")
    
    # Extracting exercise variables
    x = exercise["x"]
    y = exercise["y"]
    radix = int(exercise["radix"])
    
    answer = multiply_raw(x,y,radix)
    return {"answer": answer}

def multiply_raw(x: str, y: str, radix: int) -> str:
    # Formatting for further computations.
    sign_x = '-' if x.startswith('-') else '+'
    sign_y = '-' if y.startswith('-') else '+'
    # Remove signs for raw digit handling
    x_val = x[1:] if sign_x == '-' else x
    y_val = y[1:] if sign_y == '-' else y
    
    multiplication_case = cases[(sign_x, sign_y)]
    answer = multiplication_case(x_val, y_val, radix)
    
    return answer

# -----------------------------
# Cases
# -----------------------------

def pos_pos(x: str, y: str, radix: int) -> str:
    """
    Case: positive + positive.
    (+x) * (+y) = x * y
    """
    return multiply(x, y, radix, negative=False)

def neg_neg(x: str, y: str, radix: int) -> str:
    """
    Case: negative + negative.
    (-x) * (-y) = x * y
    Equivalent to pos_pos
    """
    return multiply(x, y, radix, negative=False)

def pos_neg(x: str, y: str, radix: int) -> str:
    """
    Case: positive + negative.
    (+x) * (-y) = -(x * y)
    """
    return multiply(x, y, radix, negative=True)

def neg_pos(x: str, y: str, radix: int) -> str:
    """
    Case: negative + postive.
    (-x) * (+y) = -(x * y)
    Equivalent to pos_neg
    """
    return multiply(x, y, radix, negative=True)

cases = {
        ('+', '+'): pos_pos,
        ('-', '-'): neg_neg,
        ('+', '-'): pos_neg,
        ('-', '+'): neg_pos,
    }