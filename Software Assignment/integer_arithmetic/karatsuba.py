from arithmetic.core import karatsuba

def multiplication_karatsuba(exercise: dict) -> dict:
    """
    Main entry point for the Karatsuba multiplication operation.

    This function extracts the input numbers and radix from the `exercise` 
    dictionary, calls `karatsuba_raw` to perform the raw computation, and 
    wraps the result in a dictionary.

    Parameters:
        exercise (dict): Contains keys 'x', 'y', and 'radix'

    Returns:
        dict: {"answer": <result_string>}
    """
    print("Executing 'multiplication (Karatsuba method)' operation...")

    # Extract input numbers and radix
    x = exercise["x"]
    y = exercise["y"]
    radix = int(exercise["radix"])

    # Compute the raw multiplication result
    answer = karatsuba_raw(x, y, radix)

    # Wrap result in a dictionary
    return {"answer": answer}


def karatsuba_raw(x: str, y: str, radix: int) -> str:
    """
    Performs multiplication using the Karatsuba algorithm, handling sign logic.

    This function determines the signs of the operands, strips them to 
    compute the multiplication using the Karatsuba algorithm on absolute 
    values, and then reapplies the correct sign to the result.

    Parameters:
        x (str): First number as string
        y (str): Second number as string
        radix (int): Base of the numbers

    Returns:
        str: Result of multiplication as string
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
    return karatsuba(x_val, y_val, radix, negative=isNegative)
