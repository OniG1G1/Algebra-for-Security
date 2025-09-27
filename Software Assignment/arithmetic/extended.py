from integer_arithmetic.subtraction import subtract_raw
from integer_arithmetic.multiplication import multiply_raw
from integer_arithmetic.division import division_raw

def extendedEuclidean(a: str, b: str, radix: int) -> tuple[str, str, str]:

    "Set up extended Euclidean table values for first two rows"
    r0, r1 = a,b
    x0, y0 = "1", "0"
    x1, y1 = "0", "1"

    "Ensure no leading 0's in a or b"
    r0 = a.lstrip("0") or "0"
    r1 = b.lstrip("0") or "0"
    
    while r1 != "0":
        "Divide a and b, and set them to q and the newest r (r2)"
        q, r2 = division_raw(r0, r1, radix)

        "x2 = x0-q*x1, must pass as dictionary to go through router"
        q_x1 = multiply_raw(q, x1, radix)
        x2 = subtract_raw(x0, q_x1, radix)

        "y2 = y0-q*y1"
        q_y1 = multiply_raw(q, y1, radix)
        y2 = subtract_raw(y0, q_y1, radix)

        "Shift values down for next iteration"
        r0, r1 = r1, r2
        x0, x1 = x1, x2
        y0, y1 = y1, y2

    "After loop is finished, r0 is the gcd(a,b), x0 and y0, are the coefficents such that x0*a + y0*b = r0"
    return (x0, y0, r0)