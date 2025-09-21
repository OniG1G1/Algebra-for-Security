from arithmetic.core import multiply

def multiplication(exercise: dict) -> dict:
    """
    Main entry point for the multiplication operation.

    This function handles sign routing and wraps the final result in a dictionary.
    It extracts the input numbers and radix from the `exercise` dictionary, 
    calls `multiply_raw` to perform the raw computation, and returns a dictionary
    containing the answer.

    Parameters:
        exercise (dict): Contains keys 'x', 'y', and 'radix'

    Returns:
        dict: {"answer": <result_string>}
    """
    print("Executing 'multiplication' operation...")
    
    # Extract input numbers and radix
    x = exercise["x"]
    y = exercise["y"]
    radix = int(exercise["radix"])
    
    # Compute the raw multiplication result
    answer = multiply_raw(x, y, radix)
    
    # Wrap result in a dictionary
    return {"answer": answer}

def multiply_raw(x: str, y: str, radix: int) -> str:
    """
    Performs the actual multiplication computation, digit-wise, handling sign logic.

    This function operates on the absolute values of x and y and routes the
    computation to the correct case function based on the combination of signs.

    Parameters:
        x (str): first number as string
        y (str): second number as string
        radix (int): base of the numbers

    Returns:
        str: result of multiplication as string
    """

    # Determine the sign of each operand
    sign_x = '-' if x.startswith('-') else '+'
    sign_y = '-' if y.startswith('-') else '+'
    
    # Strip signs for digit-wise operations
    x_val = x[1:] if sign_x == '-' else x
    y_val = y[1:] if sign_y == '-' else y
    
    # Route to the appropriate case function
    multiplication_case = cases[(sign_x, sign_y)]
    answer = multiplication_case(x_val, y_val, radix)
    
    return answer

# -----------------------------
# Sign-specific Multiplication Cases
# -----------------------------

def pos_pos(x: str, y: str, radix: int) -> str:
    """
    Case: positive * positive.
    (+x) * (+y) = x * y
    """
    return multiply(x, y, radix, negative=False)

def neg_neg(x: str, y: str, radix: int) -> str:
    """
    Case: negative * negative.
    (-x) * (-y) = x * y
    Equivalent to pos_pos
    """
    return multiply(x, y, radix, negative=False)

def pos_neg(x: str, y: str, radix: int) -> str:
    """
    Case: positive * negative.
    (+x) * (-y) = -(x * y)
    """
    return multiply(x, y, radix, negative=True)

def neg_pos(x: str, y: str, radix: int) -> str:
    """
    Case: negative * positive.
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
