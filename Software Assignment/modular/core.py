from arithmetic.core import add, subtract, multiply, karatsuba, divide
from integer_arithmetic.extended_euclidean import extendedEuclidean_raw

def modularReduction(num_str: str, radix: int, negative: bool, m:str) -> int:
    "Uses digit-wise division to find the remainder between a value and modulo m."
    x = divide(num_str, m, radix, negative)[1]
    return x.lstrip("0") or "0"

def modularKaratsuba(x: str, y: str, radix: int, negative: bool, m: str):
    "Multiplies two values in modulo m using karatsuba method."
    z = karatsuba(x, y, radix, negative)
    return modularReduction(z, radix, m, False, m)


def modularInversion(x: str, radix: int, negative: bool, m: str) -> str:
    x1, y1, gcd = extendedEuclidean_raw(x, m, radix) # Does this take into account sign handling
    print(x1, y1, gcd)
    if gcd != "1":
        print("Modular inverse does not exist") # Check if correct output
    else:
        if x1.startswith("-"):
            x1 = add(x1[1:], m, radix, False)    
        return modularReduction(x1, radix, False, m) 
    