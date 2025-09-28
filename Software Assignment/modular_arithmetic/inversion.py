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
    
    # Inversion only exists if gcd(x,m) = 1
    x1, y1, gcd = extendedEuclidean_raw(x, m, radix)

    if compare_numbers(m, "1", radix) == -1: answer = None

    if gcd != "1":
        answer = None
    else:
        answer = mod_raw(x1, m, radix)
    
    # Wrap result in a dictionary
    return {"answer": answer}
