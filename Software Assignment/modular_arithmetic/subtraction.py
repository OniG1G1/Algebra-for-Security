from arithmetic.utils import compare_numbers
from modular.core import modularAdd, modularSubtract

def subtraction(exercise: dict) -> dict: # Can we not just leave this to integer arithmetic subtraction with the extension of modular reduction
    """
    Main entry point for the subtraction operation.

    This function handles sign routing and wraps the final result in a dictionary.
    It extracts the input numbers and radix from the `exercise` dictionary, 
    calls `add_raw` to perform the raw computation, and returns a dictionary
    containing the answer.

    Parameters:
        exercise (dict): Contains keys 'x', 'y', and 'radix'

    Returns:
        dict: {"answer": <result_string>}
    """
    
    print("Executing 'subtraction' operation...")
    
    # Extract input numbers and radix
    x = exercise["x"]
    y = exercise["y"]
    radix = int(exercise["radix"])
    mod = exercise["modulus"]
    
    # Compute the raw addition result
    answer = subtract_raw(x, y, radix, mod)
    
    # Wrap result in a dictionary
    return {"answer": answer}

def subtract_raw(x: str, y: str, radix: int, mod: str) -> str:
    """
    Performs the actual subtraction computation, digit-wise, handling sign logic.

    This function operates on the absolute values of x and y and routes the
    computation to the correct case function based on the combination of signs.

    Parameters:
        x (str): first number as string
        y (str): second number as string
        radix (int): base of the numbers
        mod (str): modulus of result

    Returns:
        str: result of subtraction as string
    """

    # Determine the sign of each operand
    sign_x = '-' if x.startswith('-') else '+'
    sign_y = '-' if y.startswith('-') else '+'
    
    # Strip signs for digit-wise operations
    x_val = x[1:] if sign_x == '-' else x
    y_val = y[1:] if sign_y == '-' else y
    
    # Route to the appropriate case function
    subtraction_case = cases[(sign_x, sign_y)]
    answer = subtraction_case(x_val, y_val, radix, mod)
    
    return answer

# -----------------------------
# Sign-specific Subtraction Cases
# -----------------------------

def pos_pos(x: str, y: str, radix: int, mod: str) -> str:
    """
    Case: positive - positive.
    (+x) - (+y) = x - y
    The result may be positive or negative depending on the magnitude.
    """
    cmp = compare_numbers(x, y, radix)
    if cmp == 0:
        return "0"
    elif cmp > 0:  # x > y → result positive
        return modularSubtract(x, y, radix, False, mod)
    else:  # y > x → result negative
        return modularSubtract(y, x, radix, True, mod)

def neg_neg(x: str, y: str, radix: int, mod: str) -> str:
    """
    Case: negative - negative.
    (-x) - (-y) = (-x) + (y) = y - x
    Symmetric to pos_pos with swapped operands.
    """
    return pos_pos(y, x, radix, mod)

def pos_neg(x: str, y: str, radix: int, mod: str) -> str:
    """
    Case: positive - negative.
    (+x) - (-y) = x + y
    Result is always positive.
    """
    return modularAdd(x, y, radix, False, mod)

def neg_pos(x: str, y: str, radix: int, mod: str) -> str:
    """
    Case: negative - positive.
    (-x) - (+y) = (-x) + (-y)
    Result is always negative.
    """
    return modularAdd(x, y, radix, True, mod)
cases = {
        ('+', '+'): pos_pos,
        ('-', '-'): neg_neg,
        ('+', '-'): pos_neg,
        ('-', '+'): neg_pos,
    }