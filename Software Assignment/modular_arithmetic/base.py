from modular_arithmetic.addition import modular_addition
from modular_arithmetic.subtraction import modular_subtraction
from modular_arithmetic.reduction import reduction
from modular_arithmetic.modular_multiplication import modular_multiplication

from arithmetic.base import Arithmetic

class ModularArithmetic(Arithmetic):
    """
    Arithmetic class for modulo-based operations.
    """

    operations = {
        "reduction": reduction,
        "addition": modular_addition,
        "subtraction": modular_subtraction,
        "multiplication": modular_multiplication
        }
