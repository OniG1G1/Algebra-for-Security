from modular_arithmetic.reduction import mod_raw
from integer_arithmetic.addition import add_raw
from arithmetic.utils import compare_numbers

def modular_addition(exercise: dict) -> dict:
    """
    TODO
    """
    print("Executing 'addition' operation...")
    
    # Extract input numbers and radix
    x = exercise["x"]
    y = exercise["y"]
    radix = int(exercise["radix"])
    m = exercise["modulus"]
    
    if (compare_numbers(x, m, radix) > -1):
        x = mod_raw(x, m, radix)
    if (compare_numbers(y, m, radix) > -1):
        y = mod_raw(y, m, radix)
    
    # Compute the raw muòtiplication result
    answer = modular_add_raw(x, y, radix, m)
    
    # Wrap result in a dictionary
    return {"answer": answer}

def modular_add_raw(x_: str, y_: str, radix: int, m: str) -> str:
    if compare_numbers(m, "1", radix) == -1: return None
    z_ = add_raw(x_, y_, radix)
    return mod_raw(z_, m, radix)