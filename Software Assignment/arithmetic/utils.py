def digitParse(num_str: str) -> int:
    """
    Converts a single-digit in base 16 to an hexadecimal integer.
    """

    if num_str == "0":
        return 0
    elif num_str == "1":
        return 1
    elif num_str == "2":
        return 2
    elif num_str == "3":
        return 3
    elif num_str == "4":
        return 4
    elif num_str == "5":
        return 5
    elif num_str == "6":
        return 6
    elif num_str == "7":
        return 7
    elif num_str == "8":
        return 8
    elif num_str == "9":
        return 9
    elif num_str == "A":
        return 10
    elif num_str == "B":
        return 11
    elif num_str == "C":
        return 12
    elif num_str == "D":
        return 13
    elif num_str == "E":
        return 14
    elif num_str == "F":
        return 15
    
def reverseDigitParse(num_int: int) -> str:
    """
    Convert a single-digit base 10 integer to a hexadecimal string.
    """
    num_str = ""
    if num_int == 0:
        num_str = "0"
    if num_int == 1:
        num_str = "1"
    if num_int == 2:
        num_str = "2"
    if num_int == 3:
        num_str = "3"
    if num_int == 4:
        num_str = "4"
    if num_int == 5:
        num_str = "5"
    if num_int == 6:
        num_str = "6"
    if num_int == 7:
        num_str = "7"
    if num_int == 8:
        num_str = "8"
    if num_int == 9:
        num_str = "9"   
    if num_int == 10:
        num_str = "A"
    elif num_int == 11:
        num_str = "B"
    elif num_int == 12:
        num_str = "C"
    elif num_int == 13:
        num_str = "D"
    elif num_int == 14:
        num_str = "E"
    elif num_int == 15:
        num_str = "F"
    return num_str
    
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

def compare(self, x: str, y: str, radix: int) -> int: 
        """
        NEEDS TO BE REMADE, CANT COMPARE LONGER THAN 32 BITS
        Compare two non-negative number strings.
        Returns:
            1 if x > y
            0 if x == y
           -1 if x < y
        """
        x, y = zero_padding(x, y)
        for i in range(len(x)):
            val_x = parse(x[i], radix) 
            val_y = parse(y[i], radix)
            if val_x > val_y:
                return 1
            elif val_x < val_y:
                return -1
        return 0
    
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
