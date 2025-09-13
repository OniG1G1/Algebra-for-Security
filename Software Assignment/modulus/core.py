from arithmetic.core import add, subtract, divideRemainder

def modularReduction(num_str: str, radix: int, negative: bool, m:int) -> int:
    "Uses digit-wise division to find the remainder between a value and modulus m."
    x = divideRemainder(num_str, radix, m, negative)
    return str(x)

def modularMultiply(x: str, y: str, radix, m: int):
    "Multiplies two values in modulo m"
    x = modularReduction(x, radix, m, False, m)
    y = modularReduction(y, radix, m, False, m)
    z = int(x) * int(y)
    return modularReduction(z, radix, m, False, m)

def moduluarAdd(x: str, y: str, radix: int, negative: bool, m: int) -> str:
    """Digit-wise addition of two positive numbers in given radix in modulo m."""
    z = add(x, y, radix, negative)
    return modularReduction(z, radix, m)

def moduluarSubtract(x: str, y: str, radix: int, negative: bool, modulo: int) -> str:
    """Digit-wise subtraction: assumes x >= y, both positive in modulo m."""
    z = subtract(x, y, radix, negative)
    return modularReduction(z, radix, modulo)
