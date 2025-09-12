from utils import zero_padding

def add(self, x: str, y: str, radix: int, negative: bool) -> str:
    """Digit-wise addition of two positive numbers in given radix."""
    x, y = zero_padding(x, y)
    result = ""
    
    # TODO

    return "-" + result if negative else result

def subtract(self, x: str, y: str, radix: int, negative: bool) -> str:
    """Digit-wise subtraction: assumes x >= y, both positive."""
    x, y = zero_padding(x, y)
    result = ""
    
    # TODO
    
    return "-" + result if negative else result

    