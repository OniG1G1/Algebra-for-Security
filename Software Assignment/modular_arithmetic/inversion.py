from integer_arithmetic.extended_euclidean import extendedEuclidean_raw
from modular_arithmetic.reduction import mod_raw

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
    
    if gcd != "1":
        answer = "Modular inverse does not exist"
    else:
        answer = mod_raw(x1, m, radix)
    
    # Wrap result in a dictionary
    return {"answer": answer}
