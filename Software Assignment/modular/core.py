from arithmetic.core import add, subtract, multiply, karatsuba, divide
from arithmetic.extended import extendedEuclidean

def modularReduction(num_str: str, radix: int, negative: bool, m:str) -> int:
    "Uses digit-wise division to find the remainder between a value and modulo m."
    x = divide(num_str, m, radix, negative)[1]
    return x.lstrip("0") or "0"

def modularMultiply(x: str, y: str, radix: int, negative: bool, m: str):
    "Multiplies two values in modulo m using primary school method."
    z = multiply(x, y, radix, negative)
    return modularReduction(z, radix, m, False, m)

def modularKaratsuba(x: str, y: str, radix: int, negative: bool, m: str):
    "Multiplies two values in modulo m using karatsuba method."
    z = karatsuba(x, y, radix, negative)
    return modularReduction(z, radix, m, False, m)

def modularAdd(x: str, y: str, radix: int, negative: bool, m: str) -> str:
    "Digit-wise addition of two positive numbers in given radix in modulo m."
    z = add(x, y, radix, negative)
    return modularReduction(z, radix, False, m)

def modularSubtract(x: str, y: str, radix: int, negative: bool, m: str) -> str:
    "Digit-wise subtraction: assumes x >= y, both positive in modulo m."
    z = subtract(x, y, radix, False)
    if z.startswith("-"):
        # add modulus to z to get it positive
        z = add(z[1:], m, radix, False)  # remove minus and add modulus
    return modularReduction(z, radix, False, m)

def modularInversion(x: str, radix: int, negative: bool, m: str) -> str:
    x1, y1, gcd = extendedEuclidean(x, m, radix)
    print(x1, y1, gcd)
    if gcd != "1":
        print("Modular inverse does not exist")
    else:
        if x1.startswith("-"):
            x1 = add(x1[1:], m, radix, False)    
        return modularReduction(x1, radix, False, m) 
    