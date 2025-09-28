from modular.core import modularReduction
from integer_arithmetic.multiplication import multiply_raw 
from integer_arithmetic.subtraction import subtract_raw 
from integer_arithmetic.division import division_raw 
from arithmetic.utils import compare_numbers

class Reduction:
    def execute(self, exercise: dict) -> dict:
        """
        Main entry point for reduction.
        """
        print(f"Executing operation: {type(self).__name__}")
        x = exercise["x"]
        y = exercise["y"]

        radix = int(exercise["radix"])
        m = exercise["modulus"]
        result = modularReduction(x, y, radix, m)
        return {"answer": result}

def reduction(exercise: dict) -> dict:
    """
    TODO
    """
    print("Executing 'reduction' operation...")
    
    # Extract input numbers and radix
    x = exercise["x"]
    m = exercise["modulus"]
    radix = int(exercise["radix"])
    
    # Compute the raw reduction result
    answer = mod_raw(x, m, radix)
    
    # Wrap result in a dictionary
    return {"answer": answer} 


def mod_raw(x: str, m: str, radix: int) -> str:
    if compare_numbers(m, "1", radix) == -1: return None
    
    # Determine the sign of the operand
    sign_x = '-' if x.startswith('-') else '+'
    # Strip signs for digit-wise operations
    x_val = x[1:] if sign_x == '-' else x

    k = len(x_val)
    n = len(m)
    
    for i in range(k - n, -1, -1):
        b_i = "1" + (i * "0")
        mb_i = m + (i * "0")
        while (compare_numbers(x_val, mb_i,radix) > -1):
            x_val = subtract_raw(x_val, mb_i, radix)
    
    if ((compare_numbers(x, "0", radix) > -1) or (compare_numbers(x_val, "0", radix) == 0)):
        return subtract_raw(m, x_val, radix) if sign_x == '-' else x_val
    else:
        return subtract_raw(m, x_val, radix)  
