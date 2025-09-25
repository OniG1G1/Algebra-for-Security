#from unittest import result
from arithmetic.utils import zero_padding, parse, reverseParse, compare_magnitude

def add(x: str, y: str, radix: int, negative: bool) -> str:
    """
    Perform digit-wise addition of two numbers in an arbitrary radix (base).
    
    Args:
        x (str): First non-negative number as a string in the given radix.
        y (str): Second non-negative number as a string in the given radix.
        radix (int): The base in which the numbers are represented (e.g., 2 for binary, 10 for decimal).
        negative (bool): If True, the final result will be returned with a leading '-' sign.
    
    Returns:
        str: The result of x + y in the given radix, represented as a string.
             Includes a leading '-' if `negative` is True.
    
    Notes:
        - Input strings must contain valid digits for the specified radix.
        - The numbers are zero-padded internally to equal length.
        - Carries are handled digit by digit, starting from the least significant digit.
    """
    x, y = zero_padding(x, y)  # align both strings
    result = ""
    carry = 0
    
    # Process digits from right to left
    for i in range(len(x) - 1, -1, -1):
        x_val = parse(x[i], radix)
        y_val = parse(y[i], radix)
        
        digit_sum = x_val + y_val + carry
        carry = 0
        
        if digit_sum >= radix:
            carry = 1
            digit_sum -= radix
        
        # Convert back to digit in given radix
        result = reverseParse(digit_sum, radix) + result
    
    # Handle leftover carry
    if carry > 0: # Why not hardcode "1" since it will never be over
        result = str(carry) + result 
    
    return "-" + result if negative else result

def subtract(x: str, y: str, radix: int, negative: bool) -> str:
    """
    Perform digit-wise subtraction of two numbers in an arbitrary radix (base).

    Assumes x >= y and both numbers are positive.
    Handles borrowing digit by digit from least significant to most significant.

    Args:
        x (str): Minuend as a string in the given radix.
        y (str): Subtrahend as a string in the given radix.
        radix (int): Base of the numbers.
        negative (bool): If True, the final result will have a leading '-' sign.

    Returns:
        str: Result of x - y as a string. Leading zeros are stripped, with at least "0" returned.
             Includes '-' if `negative` is True.
    """
    # Zero-pad to equal length
    x, y = zero_padding(x, y)

    result = ""
    borrow = 0

    # Process digits from right to left
    for i in range(len(x) - 1, -1, -1):
        x_val = parse(x[i], radix)
        y_val = parse(y[i], radix)

        digit_diff = x_val - y_val - borrow
        borrow = 0

        if digit_diff < 0:
            borrow = 1
            digit_diff += radix

        # Prepend current digit to the result string
        result = reverseParse(digit_diff, radix) + result

    # Strip leading zeros
    result = result.lstrip("0") or "0"

    return "-" + result if negative else result


def multiply(x: str, y: str, radix: int, negative: bool) -> str:
    """
    Performs digit-wise multiplication of two numbers in a given radix.

    Implements schoolbook multiplication:
    - Each digit of `x` is multiplied by each digit of `y`.
    - Carries are propagated properly.
    - Intermediate results are summed using the `add` function.

    Args:
        x (str): First number as a string.
        y (str): Second number as a string.
        radix (int): Base of the numbers.
        negative (bool): Whether the result should be negative.

    Returns:
        str: The multiplication result as a string, with leading zeros removed.
             A leading '-' is prepended if `negative` is True.
    """

    x = x.lstrip("0") or "0" # Do we really need to lstrip(), when do we ever input an inproper zero-padded string
    y = y.lstrip("0") or "0"

    # Quick return if either number is zero
    if x == "0" or y == "0":
        return "0"

    results = []
    result = ""
    
    # Multiply each digit of x by each digit of y
    for i in range(len(x) - 1, -1, -1):
        temp_result = "" + (len(x) - i - 1) * "0" ### Shift for place value
        carry = 0
        for j in range(len(y) - 1, -1, -1):
            sum = 0
            x_val = parse(x[i], radix)
            y_val = parse(y[j], radix)
            sum = x_val * y_val + carry
            carry = 0
            while sum >= radix: ### Why not simply 'carry = product // radix' & 'digit = product % radix'
                sum = sum - radix
                carry += 1
                
            sum_string = reverseParse(sum, radix)
            temp_result = sum_string + temp_result
            sum_string = "" # Unnecessary
            
        if carry > 0:
            temp_result = str(carry) + temp_result
            
        # Add intermediate product to running total
        results.append(temp_result)
        while len(results) > 1:
            results[1] = add(results[0], results[1], radix, False)
            results.pop(0)
            
    result = results[0]
    
    result = results[0].lstrip("0") or "0"
    
    return "-" + result if negative else result

def karatsuba(x: str, y: str, radix: int, negative: bool) -> str:
    x = x.lstrip("0") or "0" # Again, do we REALLY need to lstrip(), when do we ever input an inproper zero-padded string
    y = y.lstrip("0") or "0"

    if x == "0" or y == "0":
        return "0"
    
    x, y = zero_padding(x, y)
    n = len(x)
    m = (n + 1) // 2
    z0 = multiply(x[m:], y[m:], radix, False)
    z2 = multiply(x[:m], y[:m], radix, False)
    left_factor = add(x[m:], x[:m], radix, False)
    right_factor = add(y[m:], y[:m], radix, False)
    z1 = subtract(multiply(left_factor, right_factor, radix, False), add(z0, z2, radix, False), radix, False)
    z1 = z1 + (n-m) * "0"
    z2 = z2 + 2 * (n-m) * "0"
    result = add(add(z0, z1, radix, False), z2, radix, False)
    return "-" + result if negative else result

def divideRemainder(x: str, y: str, radix: int, negative: bool) -> str:
    "Todo" # What????

def divide(x: str, y: str, radix: int, negative: bool) -> tuple[str, str]:
    """Assumes x,y >= 0.
       Returns a tuple result = (q, remainder)
       result[0] = q; result[1] = remainder"""
    remainder = ""
    q = ""
    for i in range(len(x)):
        remainder += x[i]
        remainder = remainder.lstrip("0") or "0"

        if (compare_magnitude(remainder, y, radix) == -1):
            q += "0"
            continue

        inter_tuple = divideIntermediate(remainder, y, radix, False)
        q += inter_tuple[0]
        remainder = inter_tuple[1]

    q = q.lstrip("0") or "0"
    q=  "-" + q if negative else q
    
    return (q, remainder)

def divideIntermediate(x: str, y: str, radix: int, negative: bool) -> tuple[str, str]:
    """Assumes x,y >= 0."""
    if y == "0":
        raise ZeroDivisionError("divide by zero") # Did you check what it says in the briefing?

    q = 0
    x = x.lstrip("0") or "0" # Same question as in 'multiply' function 
    y = y.lstrip("0") or "0"

    while compare_magnitude(x, y, radix) >= 0:
        x = subtract(x, y, radix, False).lstrip("0") or "0"
        q += 1

    q_str=  "-" + q if negative else q

    return (q_str, x)
