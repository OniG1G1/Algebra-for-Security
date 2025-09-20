#from unittest import result
from arithmetic.utils import zero_padding, parse, reverseParse, compare_magnitude

def add(x: str, y: str, radix: int, negative: bool) -> str:
    """Digit-wise addition of two positive numbers in given radix."""
    x, y = zero_padding(x, y)
    result = ""
    carry = 0
    for i in range(len(x) - 1, -1, -1):
        sum = 0
        x_val = parse(x[i], radix)
        y_val = parse(y[i], radix)
        sum = x_val + y_val + carry
        carry = 0
        if sum >= radix:
            carry = 1
            sum = sum - radix
        sum_string = reverseParse(sum, radix)
        result = sum_string + result
        sum_string = ""
    if carry > 0:
        result = str(carry) + result
    return "-" + result if negative else result

def subtract(x: str, y: str, radix: int, negative: bool) -> str:
    """Digit-wise subtraction: assumes x >= y, both positive."""
    while len(x) < len(y):
        x = "0" + x
    while len(y) < len(x):
        y = "0" + y

    result = ""
    borrow = 0
    for i in range(len(x) -1, -1, -1):
        sum = 0
        x_val = parse(x[i], radix)
        y_val = parse(y[i], radix)
        sum = x_val - y_val - borrow
        borrow = 0
        if sum < 0:
            borrow = 1
            sum = sum + radix
        sum_string = reverseParse(sum, radix)
        result = sum_string + result
        sum_string = ""

        result = result.lstrip("0") or "0"
    return "-" + result if negative else result

def multiply(x: str, y: str, radix: int, negative: bool) -> str:
    x = x.lstrip("0") or "0"
    y = y.lstrip("0") or "0"

    if x == "0" or y == "0":
        return "0"

    results = []
    result = ""
    for i in range(len(x) - 1, -1, -1):
        tempresult = "" + (len(x) - i - 1) * "0"
        carry = 0
        for j in range(len(y) - 1, -1, -1):
            sum = 0
            x_val = parse(x[i], radix)
            y_val = parse(y[j], radix)
            sum = x_val * y_val + carry
            carry = 0
            while sum >= radix:
                sum = sum - radix
                carry += 1
            sum_string = reverseParse(sum, radix)
            tempresult = sum_string + tempresult
            sum_string = ""
        if carry > 0:
            tempresult = str(carry) + tempresult
        results.append(tempresult)
        while len(results) > 1:
            results[1] = add(results[0], results[1], radix, False)
            results.pop(0)
    result = results[0]
    while len(result) > 0 and result[0] == "0":
        result = result.lstrip("0")
    return "-" + result if negative else result

def karatsuba(x: str, y: str, radix: int, negative: bool) -> str:
    x = x.lstrip("0") or "0"
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
    "Todo"

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
    if (negative):
        q = "-" + q
    
    return (q, remainder)

def divideIntermediate(x: str, y: str, radix: int, negative: bool) -> tuple[str, str]:
    """Assumes x,y >= 0."""
    if y == "0":
        raise ZeroDivisionError("divide by zero")

    q = 0
    x = x.lstrip("0") or "0"
    y = y.lstrip("0") or "0"

    while compare_magnitude(x, y, radix) >= 0:
        x = subtract(x, y, radix, False).lstrip("0") or "0"
        q += 1

    q_str = str(q)
    if negative:
        q_str = "-" + q_str

    return (q_str, x)


"""
def divideIntermediate(x: str, y: str, radix: int, negative: bool) -> tuple[str, str]:
   Assumes x,y >= 0.
    x, y = zero_padding(x, y)
    q = 0
    while (compare_magnitude(x, y, radix) >= 0):
        x = zero_padding(subtract(x, y, radix, False), y)[0]
        q += 1
    
    q = str(q)
    if (negative):
        q = "-" + q
    
    return (q, x)
"""
