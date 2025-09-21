from arithmetic.utils import compare_numbers
from arithmetic.core import add, subtract
    
def subtraction(exercise: dict) -> dict:
    
    """
    Main entry point for subtraction. Handles sign routing.
    """
    
    print("Executing 'subtraction' operation...")
    
    # Extracting exercise variables.
    x = exercise["x"]
    y = exercise["y"]
    radix = int(exercise["radix"])
    
    answer = subtract_raw(x, y, radix)
    
    # Wraps in a dictionary.
    return {"answer": answer}

def subtract_raw(x: str, y: str, radix: int) -> str:
    
    # Formatting for further computations.
    sign_x = '-' if x.startswith('-') else '+'
    sign_y = '-' if y.startswith('-') else '+'
    # Remove signs for raw digit handling
    x_val = x[1:] if sign_x == '-' else x
    y_val = y[1:] if sign_y == '-' else y
    
    subtraction_case = cases[(sign_x, sign_y)]
    answer = subtraction_case(x_val, y_val, radix)
    
    return answer

# -----------------------------
# Cases
# -----------------------------

def pos_pos(x: str, y: str, radix: int) -> str:
        """
        Case: positive - positive.
        (+x) - (+y) = x - y
        """
        cmp = compare_numbers(x, y, radix)
        if cmp == 0:
            return "0"
        elif cmp > 0:  # x > y → result positive
            return subtract(x, y, radix, negative=False)
        else:  # y > x → result negative
            return subtract(y, x, radix, negative=True)

def neg_neg(x: str, y: str, radix: int) -> str:
        """
        Case: negative - negative.
        (-x) - (-y) = (-x) + (y) = y - x
        """
        return pos_pos(y, x, radix)

def pos_neg(x: str, y: str, radix: int) -> str:
        """
        Case: positive - negative.
        (+x) - (-y) = x + y
        """
        return add(x, y, radix, negative=False)

def neg_pos(x: str, y: str, radix: int) -> str:
        """
        Case: positive - positive.
        (-x) - (+y) = (-x) + (-y)
        """
        return add(x, y, radix, negative=True)

cases = {
        ('+', '+'): pos_pos,
        ('-', '-'): neg_neg,
        ('+', '-'): pos_neg,
        ('-', '+'): neg_pos,
    }