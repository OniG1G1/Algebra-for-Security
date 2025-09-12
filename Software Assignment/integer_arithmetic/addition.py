from arithmetic.utils import compare_magnitude
from arithmetic.core import add, subtract

class Addition:
    def execute(self, exercise: dict) -> dict:
        """
        Main entry point for addition. Handles sign routing.
        """
        print(f"Executing operation: {type(self).__name__}")
        x = exercise["x"]
        y = exercise["y"]
        radix = int(exercise["radix"])

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
        result = handler(x_val, y_val, radix)

        return {"answer": result}

    # -----------------------------
    # Cases
    # -----------------------------

    def _pos_pos(self, x: str, y: str, radix: int) -> str:
        """
        Case: positive + positive.
        (+x) + (+y) = x + y
        """
        return add(x, y, radix, negative=False)

    def _neg_neg(self, x: str, y: str, radix: int) -> str:
        """
        Case: negative + negative.
        (-x) + (-y) = - (x + y)
        """
        return add(x, y, radix, negative=True)

    def _pos_neg(self, x: str, y: str, radix: int) -> str:
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
            return subtract(x, y, radix, negative=False)
        else:  # y > x → result negative
            return subtract(y, x, radix, negative=True)

    def _neg_pos(self, x: str, y: str, radix: int) -> str:
        """
        Case: negative + postive.
        (-x) + (y) = y - x
        Symmetric to pos_neg
        """
        return self._pos_neg(y, x, radix)