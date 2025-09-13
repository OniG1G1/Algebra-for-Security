from utils import zero_padding, parse, reverseParse, digitParse

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
    x, y = zero_padding(x, y)
    result = ""
    borrow = 0
    for i in range(len(x) - 1, -1, -1):
        sum = 0
        x_val = parse(x[i], radix)
        y_val = parse(y[i], radix)
        sum = x_val - y_val - borrow
        borrow = 0
        if sum < 0:
            borrow = 1
            sum = sum + radix
        sum_string = str(reverseParse(sum, radix))
        result = sum_string + result
        sum_string = ""
    return "-" + result if negative else result

def divideRemainder(x: str, y: str, radix: int, negative: bool) -> str:
    "Todo"

def divideQuotient(x: str, y: str, radix: int, negative: bool) -> str:
    "Todo"