from arithmetic.core import divide

def division_raw(x: str, y: str, radix: int) -> str:
    """
    Performs the actual division computation, digit-wise, handling sign logic.

    This function operates on the absolute values of x and y and routes the
    computation to the correct case function based on the combination of signs.

    Parameters:
        x (str): Dividend as a string
        y (str): Divisor as a string
        radix (int): Base of the numbers

    Returns:
        str: Result of division as string
    """
    # Determine the sign of each operand
    sign_x = '-' if x.startswith('-') else '+'
    sign_y = '-' if y.startswith('-') else '+'
    
    # Strip signs for digit-wise operations
    x_val = x[1:] if sign_x == '-' else x
    y_val = y[1:] if sign_y == '-' else y
    
    # Route to the appropriate case function
    division_case = cases[(sign_x, sign_y)]
    answer = division_case(x_val, y_val, radix)
    
    return answer

# -----------------------------
# Sign-specific Division Cases
# -----------------------------

def pos_pos(x: str, y: str, radix: int) -> str:
    """
    Case: positive ÷ positive.
    (+x) ÷ (+y) = x ÷ y
    """
    return divide(x, y, radix, negative=False)

def neg_neg(x: str, y: str, radix: int) -> str:
    """
    Case: negative ÷ negative.
    (-x) ÷ (-y) = x ÷ y
    Equivalent to pos_pos
    """
    return divide(x, y, radix, negative=False)

def pos_neg(x: str, y: str, radix: int) -> str:
    """
    Case: positive ÷ negative.
    (+x) ÷ (-y) = -(x ÷ y)
    """
    return divide(x, y, radix, negative=True)

def neg_pos(x: str, y: str, radix: int) -> str:
    """
    Case: negative ÷ positive.
    (-x) ÷ (+y) = -(x ÷ y)
    Equivalent to pos_neg
    """
    return divide(x, y, radix, negative=True)

cases = {
    ('+', '+'): pos_pos,
    ('-', '-'): neg_neg,
    ('+', '-'): pos_neg,
    ('-', '+'): neg_pos,
}
