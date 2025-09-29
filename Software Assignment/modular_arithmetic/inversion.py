from integer_arithmetic.extended_euclidean import extendedEuclidean_raw
from modular_arithmetic.reduction import mod_raw
from arithmetic.utils import compare_numbers

def modular_inversion(exercise: dict) -> dict:
    """
    TODO
    """
    print("Executing 'inversion' operation...")
    
    # Extract input numbers and radix
    x = exercise["x"]
    m = exercise["modulus"]
    radix = int(exercise["radix"])

    sign_x = '-' if x.startswith('-') else '+'
    x_val = x[1:] if sign_x == '-' else x
    
    # Inversion only exists if gcd(x,m) = 1
    x1, y1, gcd = extendedEuclidean_raw(x_val, m, radix)

    if compare_numbers(m, "1", radix) == -1: answer = None

    if sign_x == '-' and x1 != "0":
        if not x1.startswith("-"):
            x1 = "-" + x1
        else:
            x1 = x1[1:]

    if gcd != "1":
        answer = None
    else:
        answer = mod_raw(x1, m, radix)
    
    # Wrap result in a dictionary
    return {"answer": answer}
