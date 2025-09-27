def digitParse(num_str: str) -> int:
    """
    Converts a single-digit in base 16 to an hexadecimal integer.
    """
    DIGITS = "0123456789ABCDEF"
    return DIGITS.find(num_str) 
    
def reverseDigitParse(num_int: int) -> str:
    """
    Convert a single-digit base 10 integer to a hexadecimal string.
    """
    DIGITS = "0123456789ABCDEF"
    return DIGITS[num_int]
    
def parse(num_str: str, radix: int) -> int:
    """
    Convert a single-digit or full number string in a given radix to a base 10 integer.
    """
    set_neg = False
    if "-" in num_str:
        num_str.replace("-", "")
        set_neg = True

    power = 0
    total_sum = 0
    for i in range(len(num_str)-1, -1, -1):
        digit_val = digitParse(num_str[i])
        digit_sum = digit_val * radix**power
        power += 1
        total_sum = total_sum + digit_sum
    if set_neg == True:
        return -total_sum
    else:
        return total_sum 

def reverseParse(num_int: int, radix: int) -> str:
    """
    Convert a single-digit or full number base 10 integer into a string with a given radix.
    """
    set_neg = False
    if num_int < 0:
        num_int = abs(num_int)
        set_neg = True
    divided = num_int
    if num_int == 0:
        num_str = "0" 
    else:    
        num_str = ""
    digit = ""
    while divided != 0:
        digit = reverseDigitParse(divided % radix)
        num_str = digit + num_str
        divided = (divided // radix)
    if set_neg:
            return "-" + num_str
    else:
        return num_str

def zero_padding(x: str, y: str) -> tuple[str, str]:
    """
    Pad the shorter of two number strings with leading zeros
    so that both strings have the same length.
    """
    length_diff = len(x) - len(y)
    padding = "0" * abs(length_diff)
    if length_diff > 0:
        # x is longer; pad y
        y = padding + y
    elif length_diff < 0:
        # y is longer; pad x
        x = padding + x
    return x, y
    
def compare_magnitude(x: str, y: str, radix: int) -> int:
    """
    Compare two positive integers represented as strings in given radix.
    Returns:
        1 if x > y
        -1 if x < y
        0 if equal
    """
    x = x.lstrip("0") or "0"
    y = y.lstrip("0") or "0"

    if len(x) > len(y):
        return 1
    if len(x) < len(y):
        return -1

    for i in range(len(x)):
        digit_x = parse(x[i], radix)
        digit_y = parse(y[i], radix)
        if digit_x > digit_y:
            return 1
        elif digit_x < digit_y:
            return -1
    return 0

def compare_numbers(x: str, y: str, radix: int) -> int:
    """
    Compare two non-negative integer strings in the given radix.

    Args:
        x (str): First number string.
        y (str): Second number string.
        radix (int): Base of the number system (e.g., 2, 10, 16).

    Returns:
        int: 1 if x > y, -1 if x < y, 0 if equal.
    """

    # Normalize inputs (strip leading zeros but keep at least one digit)
    x = x.lstrip("0") or "0"
    y = y.lstrip("0") or "0"

    # First compare by length → avoids expensive digit parsing
    if len(x) > len(y):
        return 1
    if len(x) < len(y):
        return -1

    # If same length, compare digit by digit
    for digit_x, digit_y in zip(x, y):
        val_x = parse(digit_x, radix)
        val_y = parse(digit_y, radix)
        if val_x > val_y:
            return 1
        elif val_x < val_y:
            return -1

    return 0

