from addition import addition
from integer_arithmetic.subtraction import Subtraction
from integer_arithmetic.multiplication import Multiplication
from integer_arithmetic.karatsuba import Karatsuba
from integer_arithmetic.extended_euclidean import ExtendedEuclidean
from arithmetic.base import Arithmetic

class IntegerArithmetic(Arithmetic):
    """
    Arithmetic class for integer-based operations.
    """

    operations = {
        "addition": addition,
        "subtraction": Subtraction().execute,
        "multiplication": Multiplication().execute,
        "multiplication_primary": Multiplication().execute,
        "multiplication_karatsuba": Karatsuba().execute,
        "extended_euclidean_algorithm": ExtendedEuclidean().execute,
    }
