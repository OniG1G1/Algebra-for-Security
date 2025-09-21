from arithmetic.utils import compare_numbers
from arithmetic.core import add, subtract

def addition(exercise: dict) -> dict:
    
    """
    Main entry point for addition. Handles sign routing.
    """
    
    print("Executing 'addition' operation...")
    
    # Extracting exercise variables
    x = exercise["x"]
    y = exercise["y"]
    radix = int(exercise["radix"])
    
    answer = add_raw(x, y, radix)
    return {"answer": answer}

def add_raw(x: str, y: str, radix: int) -> str:
    
    # Formatting for further computations
    sign_x = '-' if x.startswith('-') else '+'
    sign_y = '-' if y.startswith('-') else '+'
    
    # Remove signs for raw digit handling
    x_val = x[1:] if sign_x == '-' else x
    y_val = y[1:] if sign_y == '-' else y
    
    addition_case = cases[(sign_x, sign_y)]
    answer = addition_case(x_val, y_val, radix)
    
    return answer

# -----------------------------
# Cases
# -----------------------------

def pos_pos(x: str, y: str, radix: int) -> str:
    """
    Case: positive + positive.
    (+x) + (+y) = x + y
    """
    return add(x, y, radix, negative=False)

def neg_neg(x: str, y: str, radix: int) -> str:
        """
        Case: negative + negative.
        (-x) + (-y) = - (x + y)
        """
        return add(x, y, radix, negative=True)

def pos_neg( x: str, y: str, radix: int) -> str:
        """
        Case: positive + negative.
        (x) + (-y) = x - y
        """
        
        cmp = compare_numbers(x, y, radix)
        if cmp == 0:
            return "0"
        elif cmp > 0:  # x > y → result positive
            return subtract(x, y, radix, negative=False)
        else:  # y > x → result negative
            return subtract(y, x, radix, negative=True)

def neg_pos(x: str, y: str, radix: int) -> str:
        """
        Case: negative + postive.
        (-x) + (y) = y - x
        Symmetric to pos_neg
        """
        return pos_neg(y, x, radix)

cases = {
        ('+', '+'): pos_pos,
        ('-', '-'): neg_neg,
        ('+', '-'): pos_neg,
        ('-', '+'): neg_pos,
    }