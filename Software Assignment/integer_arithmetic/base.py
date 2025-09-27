from integer_arithmetic.addition import addition
from integer_arithmetic.subtraction import subtraction
from integer_arithmetic.multiplication import multiplication
from integer_arithmetic.karatsuba import multiplication_karatsuba
from integer_arithmetic.extended_euclidean import extended_euclidean
from arithmetic.base import Arithmetic

class IntegerArithmetic(Arithmetic):
    """
    Arithmetic class for integer-based operations.
    """

    operations = {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication_primary": multiplication,
        "multiplication_karatsuba": multiplication_karatsuba,
        "extended_euclidean_algorithm": extended_euclidean,
    }
