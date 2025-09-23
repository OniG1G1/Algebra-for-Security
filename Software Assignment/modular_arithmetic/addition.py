from arithmetic.utils import compare_magnitude
from modular.core import modularAdd, modularSubtract

class Addition:
    def execute(self, exercise: dict) -> dict:
        """
        Main entry point for addition. Handles sign routing.
        """
        print(f"Executing operation: {type(self).__name__}")
        x = exercise["x"]
        y = exercise["y"]
        radix = int(exercise["radix"])
        m = exercise["modulus"]

        sign_x = '-' if x.startswith('-') else '+'
        sign_y = '-' if y.startswith('-') else '+'

        # Remove signs for raw digit handling
        x_val = x[1:] if sign_x == '-' else x
        y_val = y[1:] if sign_y == '-' else y

        router = {
            ('+', '+'): self._pos_pos,
            ('-', '-'): self._neg_neg,
            ('+', '-'): self._pos_neg,
            ('-', '+'): self._neg_pos,
        }

        handler = router[(sign_x, sign_y)]
        result = handler(x_val, y_val, radix, m)

        return {"answer": result}

    # -----------------------------
    # Cases
    # -----------------------------

    def _pos_pos(self, x: str, y: str, radix: int, m: int) -> str:
        """
        Case: positive + positive.
        (+x) + (+y) = x + y
        """
        return modularAdd(x, y, radix, negative=False, m=m)

    def _neg_neg(self, x: str, y: str, radix: int, m: int) -> str:
        """
        Case: negative + negative.
        (-x) + (-y) = - (x + y)
        """
        return modularAdd(x, y, radix, negative=True, m=m)

    def _pos_neg(self, x: str, y: str, radix: int, m: int) -> str:
        """
        Case: positive + negative.
        (x) + (-y) = x - y
        """
        # strip any leading signs
        x = x.lstrip('-')
        y = y.lstrip('-')
        
        cmp = compare_magnitude(x, y, radix)
        if cmp == 0:
            return "0"
        elif cmp > 0:  # x > y → result positive
            return modularSubtract(x, y, radix, negative=False, m=m)
        else:  # y > x → result negative
            return modularSubtract(y, x, radix, negative=True, m=m)

    def _neg_pos(self, x: str, y: str, radix: int, m: int) -> str:
        """
        Case: negative + postive.
        (-x) + (y) = y - x
        Symmetric to pos_neg
        """
        return self._pos_neg(y, x, radix, m)