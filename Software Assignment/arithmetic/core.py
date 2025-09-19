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

def multiply(x: str, y: str, radix: int, negative: bool) -> str:
    x, y = zero_padding(x, y)
    results = []
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
    return "-" + results[0] if negative else results[0]

def karatsuba(x: str, y: str, radix: int, negative: bool) -> str:
    n = max(len(x), len(y))
    m = n // 2
    z0 = multiply(x[m:], y[m:], radix, False)
    z2 = multiply[x[:m], y[:m], radix, False]
    left_factor = add(x[m:], x[:m], radix, False)
    right_factor = add(y[m:], y[:m], radix, False)
    z1 = subtract(multiply(left_factor, right_factor, radix, False), add(z0, z2, radix, False), radix, False)
    z0 = (m - len(z0)) * "0"
    z1 = (m - len(z1)) * "0"
    result = z2 + z1 + z0
    return "-" + result if negative else result

def divideRemainder(x: str, y: str, radix: int, negative: bool) -> str:
    "Todo"

def divideQuotient(x: str, y: str, radix: int, negative: bool) -> str:
    "Todo"