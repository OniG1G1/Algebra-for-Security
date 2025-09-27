from modular_arithmetic.addition import addition
#from modular_arithmetic.subtraction import subtraction
from modular_arithmetic.reduction import reduction

from arithmetic.base import Arithmetic

class ModularArithmetic(Arithmetic):
    """
    Arithmetic class for modulo-based operations.
    """

    operations = {
        "addition": addition,
        #"subtraction": subtraction,
        "reduction": reduction
        }
