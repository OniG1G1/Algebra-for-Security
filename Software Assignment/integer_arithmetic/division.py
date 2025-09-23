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
    
    # Result sign: same signs -> positive, different signs -> negative
    isNegative = (sign_x != sign_y)
    
    # Perform division with sign
    return divide(x_val, y_val, radix, negative=isNegative)

