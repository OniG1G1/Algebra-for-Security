def parse(num_str: str, radix: int) -> int:
    """
    Convert a single-digit or full number string in a given radix to an integer.
    Works for radix 2-16.
    """
    return int(num_str, radix)


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
    if len(x) > len(y):
        return 1
    if len(x) < len(y):
        return -1

    for i in range(len(x)):
        digit_x = int(x[i], radix)
        digit_y = int(y[i], radix)
        if digit_x > digit_y:
            return 1
        elif digit_x < digit_y:
            return -1
    return 0


#Convert Python int into string representation in given radix.
    #def format(self, num: int, radix: int) -> str:
    #    if num == 0:
    #        return "0"
#
    #    neg = num < 0
    #    num = abs(num)
    #    result = ""
#
    #    while num > 0:
    #        result = self.DIGITS[num % radix] + result
    #        num //= radix
#
    #    return "-" + result if neg else result
