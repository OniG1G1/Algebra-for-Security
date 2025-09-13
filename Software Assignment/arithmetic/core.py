from utils import zero_padding, parse, reverseParse

def add(x: str, y: str, radix: int, negative: bool, modulo: int) -> str:
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
        
        sum_string = hex(sum)[2:]
        sum_string = str(sum_string)
        result = sum_string + result
        sum_string = ""
    if carry > 0:
        result = str(carry) + result

    if (modulo != -1):
        result_int = int(result, radix)
        result_int = result_int % modulo
        result = hex(result_int)[2:]
        result = str(result)
    return "-" + result if negative else result

def subtract(x: str, y: str, radix: int, negative: bool, modulo: int) -> str:
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
        sum_string = hex(sum)[2:]
        sum_string = str(sum_string)
        "sum_string = str(sum)"
        result = sum_string + result
        sum_string = ""
    assert borrow == 0, "unexpected borrow, swap x and y"
    if (modulo != -1):
        result_int = int(result, radix)
        result_int = result_int % modulo
        result = hex(result_int)[2:]
        result = str(result)
    return "-" + result if negative else result

def addSimple(x: str, y: str, radix: int, negative: bool, modulo: int) -> str:
    x_int = parse(x, radix)
    y_int = parse(y, radix)
    z = x_int + y_int
    if negative:
        z = -abs(z)
    if modulo > -1:
        z = modularReduction(z, modulo)
    return reverseParse(z, radix)

def subtractSimple(x: str, y: str, radix: int, negative: bool, modulo: int) -> str:
    x_int = parse(x, radix)
    y_int = parse(y, radix)
    z = x_int - y_int
    if negative:
        z = -abs(z)
    if modulo > -1:
        z = modularReduction(z, modulo)
    return reverseParse(z, radix)

def divideQuotient(x: str, y: str, radix: int) -> str:
    x_int = parse(x, radix)
    y_int = parse(y, radix)
    z = x_int // y_int
    return reverseParse(z, radix)

def divideRemainder(x: str, y: str, radix: int) -> str:
    x_int = parse(x, radix)
    y_int = parse(y, radix)
    z = x_int % y_int
    return reverseParse(z, radix)

def modularReduction(x: int, modulo: int) -> int:
    return x % modulo

"def modularMultiply(x: int, y: int, m):"
