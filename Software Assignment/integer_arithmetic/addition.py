from arithmetic.utils import zero_padding, compare_magnitude

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
        """Case: positive + positive."""
        return self._add(x, y, radix, negative=False)

    def _neg_neg(self, x: str, y: str, radix: int) -> str:
        """Case: negative + negative."""
        return self._add(x, y, radix, negative=True)

    def _pos_neg(self, x: str, y: str, radix: int) -> str:
        """Case: positive + negative."""
        cmp = compare_magnitude(x, y, radix)
        if cmp == 0:
            return "0"
        elif cmp > 0:  # x > y → result positive
            return self._subtract(x, y, radix, negative=False)
        else:  # y > x → result negative
            return self._subtract(y, x, radix, negative=True)

    def _neg_pos(self, x: str, y: str, radix: int) -> str:
        """Case: negative + positive."""
        # Symmetric to pos_neg
        return self._pos_neg(y, x, radix)

    # -----------------------------
    # Core digit-wise helpers
    # -----------------------------

    def _add(self, x: str, y: str, radix: int, negative: bool) -> str:
        """Digit-wise addition of two positive numbers in given radix."""
        x, y = zero_padding(x, y)
        carry = 0
        result = ""

        for i in range(len(x) - 1, -1, -1):
            digit_sum = int(x[i], radix) + int(y[i], radix) + carry
            carry = digit_sum // radix
            result = str(digit_sum % radix) + result

        if carry:
            result = str(carry) + result

        return "-" + result if negative else result

    def _subtract(self, x: str, y: str, radix: int, negative: bool) -> str:
        """Digit-wise subtraction: assumes x >= y, both positive."""
        x, y = zero_padding(x, y)
        borrow = 0
        result = ""

        for i in range(len(x) - 1, -1, -1):
            diff = int(x[i], radix) - int(y[i], radix) - borrow
            if diff < 0:
                diff += radix
                borrow = 1
            else:
                borrow = 0
            result = str(diff) + result

        result = result.lstrip("0") or "0"
        return "-" + result if negative else result
